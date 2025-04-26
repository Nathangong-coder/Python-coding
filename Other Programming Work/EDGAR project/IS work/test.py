from dataclasses import dataclass
from typing import List, Optional, Dict, Tuple
from datetime import datetime
import os
from pathlib import Path
import sqlite3
from bs4 import BeautifulSoup
from openai import OpenAI
import json
from dotenv import load_dotenv
import re
from itertools import islice

@dataclass
class Education:
    degree: str
    field: str
    university: str
    year: Optional[int] = None

@dataclass
class Executive:
    name: str
    age: Optional[int]
    current_role: str
    past_roles: List[str]
    education: List[Education]
    compensation_salary: float
    compensation_stock: float
    compensation_bonus: float
    compensation_other: float
    compensation_total: float
    compensation_year: int
    start_date: Optional[str]
    board_member: bool
    committee_memberships: List[str]
    other_board_memberships: List[str]
    notable_achievements: Optional[str]

def init_db():
    """Initialize database with fresh tables for executive data"""
    db_path = 'def14a_filings/filings.db'

    with sqlite3.connect(db_path) as conn:
        # Clear existing tables if they exist
        conn.execute("DROP TABLE IF EXISTS executive_data")
        conn.execute("DROP TABLE IF EXISTS processing_status")

        # Create new tables
        conn.execute("""
            CREATE TABLE executive_data (
                cik TEXT,
                filing_date TEXT,
                exec_name TEXT,
                data JSON,
                last_updated TIMESTAMP,
                PRIMARY KEY (cik, filing_date, exec_name)
            )
        """)

        conn.execute("""
            CREATE TABLE processing_status (
                cik TEXT PRIMARY KEY,
                filing_date TEXT,
                status TEXT,
                error_msg TEXT,
                last_updated TIMESTAMP
            )
        """)

def extract_sections(content: str, headings: List[Tuple[str, float]]) -> Dict[str, str]:
    """Extract sections using identified headings"""
    soup = BeautifulSoup(content, 'html.parser')
    sections = {}

    # Get all text elements
    text_elements = [elem.strip() for elem in soup.find_all(string=True) if elem.strip()]

    # Sort headings by confidence
    headings = sorted(headings, key=lambda x: x[1], reverse=True)

    for i, (heading, _) in enumerate(headings):
        try:
            start_idx = next(idx for idx, text in enumerate(text_elements)
                           if heading in text)

            # Find next heading
            end_idx = len(text_elements)
            for next_heading, _ in headings[i+1:]:
                try:
                    next_idx = next(idx for idx, text in enumerate(text_elements[start_idx+1:], start_idx+1)
                                  if next_heading in text)
                    if next_idx < end_idx:
                        end_idx = next_idx
                except StopIteration:
                    continue

            content = '\n'.join(text_elements[start_idx+1:end_idx])
            if len(content) > 100:
                sections[heading] = content

        except StopIteration:
            continue
    print(list(sections)[:5])
    return sections

def identify_headings(content: str) -> List[Tuple[str, float]]:
    """Identify potential section headings using multiple heuristics"""
    soup = BeautifulSoup(content, 'html.parser')
    headings = []

    # Traditional heading tags
    for tag in ['h1', 'h2', 'h3']:
        for h in soup.find_all(tag):
            headings.append((h.get_text().strip(), 0.9))

    # CSS class-based detection
    heading_patterns = ['heading', 'title', 'header', 'section']
    for elem in soup.find_all(class_=re.compile('|'.join(heading_patterns), re.I)):
        headings.append((elem.get_text().strip(), 0.8))

    # Font style based detection
    for elem in soup.find_all(style=re.compile('(font-weight.*?bold|font-size.*?1[2-9]px)', re.I)):
        text = elem.get_text().strip()
        if len(text) < 100:
            headings.append((text, 0.7))

    # Text pattern detection
    for elem in soup.find_all(string=True):
        text = elem.strip()
        if text and len(text) < 100:
            if text.isupper() and len(text) > 10:
                headings.append((text, 0.6))
            elif text.endswith(':'):
                headings.append((text, 0.5))

    # Deduplicate and clean
    seen = set()
    unique_headings = []
    for text, score in headings:
        text = re.sub(r'\s+', ' ', text).strip()
        if text and text not in seen and len(text) < 200:
            seen.add(text)
            unique_headings.append((text, score))
    print(list(unique_headings[:5]))
    return unique_headings

def get_compensation_section(sections: Dict[str, str]) -> Optional[Dict[str, str]]:
    """Find relevant sections containing executive information"""
    relevant_sections = {}

    # Keywords for different types of information
    section_keywords = {
        'compensation': [
            'summary compensation table',
            'executive compensation',
            'compensation discussion',
            'director compensation'
        ],
        'biography': [
            'executive officers',
            'board of directors',
            'biographical information',
            'director nominees'
        ]
    }

    # Check each section
    for heading, content in sections.items():
        heading_lower = heading.lower()
        for category, keywords in section_keywords.items():
            if any(k in heading_lower for k in keywords) or \
               any(k in content.lower()[:1000] for k in keywords):
                if category == 'compensation':
                    continue  # Skip compensation sections without tables
                relevant_sections[heading] = content
    print(relevant_sections)
    return relevant_sections if relevant_sections else None

#MAIN CODING PROBLEM FUNCTION
def process_companies():
    """Process all companies, only looking at their latest filing"""
    load_dotenv()

    db_path = 'def14a_filings/filings.db'

    with sqlite3.connect(db_path) as conn:
        # Get latest filing for each company
        companies = conn.execute("""
            WITH latest_filings AS (
                SELECT f.cik, f.filing_date, f.file_path, c.name,
                       ROW_NUMBER() OVER (PARTITION BY f.cik ORDER BY f.filing_date DESC) as rn
                FROM filings f
                JOIN companies c ON f.cik = c.cik
                WHERE f.status = 'completed'
            )
            SELECT cik, name, filing_date, file_path
            FROM latest_filings
            WHERE rn = 1
            ORDER BY filing_date DESC
        """).fetchall()

        for cik, name, filing_date, file_path in companies:
            # Skip if already processed
            status = conn.execute(
                "SELECT status FROM processing_status WHERE cik = ?",
                (cik,)
            ).fetchone()

            if status and status[0] == 'completed':
                print(f"Skipping {name} - already processed")
                continue

            print(f"\nProcessing {name} (CIK: {cik})")

            # Read filing content
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extract sections using robust parsing
            headings = identify_headings(content)
            sections = extract_sections(content, headings)
            print(get_compensation_section(sections))


init_db()
process_companies()

