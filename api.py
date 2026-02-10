import requests
import pandas as pd
import time
import json

# Replace with your actual values
DOMAIN = "qtestnet.com"
PROJECT_ID = "test"
TOKEN = "YOUR_BEARER_TOKEN"
DEFECT_IDS = [, ...] # Your list of 8405 IDs

headers = {"Authorization": f"bearer {TOKEN}", "Content-Type": "application/json"}
all_comments = []

# Using a loop to fetch and tie
for i, d_id in enumerate(DEFECT_IDS):
    url = f"https://{DOMAIN}/api/v3/projects/{PROJECT_ID}/defects/{d_id}/comments"
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            comments = response.json()
            for cmt in comments:
                # THE TIE: Injecting the parent ID manually
                cmt['parent_defect_id'] = d_id 
                all_comments.append(cmt)
        
        # Rate Limiting: 2 requests per second is safe for qTest
        time.sleep(0.5) 
        
        # Checkpoint: Save every 500 defects so you don't lose data
        if i % 500 == 0:
            pd.DataFrame(all_comments).to_csv(f"comments_checkpoint_{i}.csv", index=False)
            print(f"Processed {i} defects...")

    except Exception as e:
        print(f"Error at defect {d_id}: {e}")

# Final Flattening into a DataFrame
df_comments = pd.DataFrame(all_comments)
df_comments.to_csv("all_qtest_comments_final.csv", index=False)
