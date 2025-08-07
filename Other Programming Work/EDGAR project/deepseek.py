from openai import OpenAI
prompt=input("Hello, welcome to OpenAI! Enter your bridge-related prompt:")
response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are an expert bridge teacher with 25+ years of experience crafting tournament-level problems. Your exercises focus on defensive carding in suit contracts, specifically middle-of-the-hand leads where defenders must disrupt declarer's timing. This exercise includes realistic bidding (2/1 GF system), validated deals (all 13-card hands), and strict adherence to bridge mechanics (declarer identity, lead rotation, trick sequencing). Your task is to analyze the provided bridge deal and identify the most relevant sections for the user."},
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": "I will identify the most relevant sections and return them as a JSON array."},
                {"role": "user", "content": json.dumps(section_previews, indent=2)}
            ],
            temperature=0.1
        )