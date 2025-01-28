import requests
import pandas as pd
from bs4 import BeautifulSoup
import os
from pathlib import Path
import logging
import re

class FinancialDataExtractor:
    def __init__(self, email: str, output_dir: str = "financial_data"):
        self.headers = {
            'User-Agent': f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 {email}'
        }
        self.base_url = "https://www.sec.gov/Archives"
        self.output_dir = output_dir
        Path(output_dir).mkdir(exist_ok=True)
        self._setup_logging()

    def _setup_logging(self):
        log_file = os.path.join(self.output_dir, 'financial_extractor.log')
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )
        self.logger = logging

    def _make_request(self, url: str) -> str:
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.text

    def get_filing_links(self, cik: str, filing_type: str = "10-K", limit: int = 5):
        url = f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={cik}&type={filing_type.replace(' ', '+')}&count={limit}"
        response = self._make_request(url)
        soup = BeautifulSoup(response, 'html.parser')

        filings = []
        for row in soup.find_all('tr')[1:]:
            cols = row.find_all('td')
            if len(cols) >= 4:
                doc_link = cols[1].find('a')
                if doc_link:
                    filings.append(f"https://www.sec.gov{doc_link['href']}")
        return filings

    def get_filing_content(self, filing_url: str):
        filing_page = self._make_request(filing_url)
        soup = BeautifulSoup(filing_page, 'html.parser')
        doc_link = None
        for link in soup.find_all('a'):
            if '.htm' in link.get('href', '').lower():
                doc_link = f"https://www.sec.gov{link['href']}"
                break
        return self._make_request(doc_link) if doc_link else None

    def extract_financial_data(self, filing_content: str):
        data_points = {}
        search_patterns = {
            'cash_flow': r'Cash\s+Flow',
            'capital_expenditures': r'Capital\s*Expenditures.*?\$(\d+[,.\d]*)',
            'net_income': r'Net\s+Income',
            'shareholder_equity': r'Shareholder\s+Equity',
            'proxy_statement': r'proxy\s+statement',
            'executive_compensation': r'(executive\s+compensation|compensation\s+discussion)',
            'board_of_directors': r'(board\s+of\s+directors|corporate\s+governance)',
            'ownership_holdings': r'(stock|share)\s+(ownership|holdings)',
        }

        for key, pattern in search_patterns.items():
            match = re.search(pattern, filing_content, re.IGNORECASE)
            data_points[key] = match.group(1) if match else 'N/A'

        return data_points

    def process_company_filings(self, cik: str):
        filings = self.get_filing_links(cik)
        for filing_url in filings:
            content = self.get_filing_content(filing_url)
            if content:
                financial_data = self.extract_financial_data(content)
                self.logger.info(f"Financial data for CIK {cik}: {financial_data}")
                pd.DataFrame([financial_data]).to_csv(
                    os.path.join(self.output_dir, f'{cik}_financials.csv'), index=False
                )

if __name__ == "__main__":
    email = "your_email@example.com"  # Replace with your email
    extractor = FinancialDataExtractor(email)
    test_cik = "0000320193"  # Example CIK for Apple
    extractor.process_company_filings(test_cik)
