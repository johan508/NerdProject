#!/usr/bin/env python
# coding: utf-8

# In[78]:


# Created by Han Zhang (you can copy it but pls put my name on it, if it doesn't work for you, email me)
import requests
import csv
import pandas as pd
import matplotlib.pyplot as plt


# In[79]:


APP_ID = '829cd6b1'
APP_KEY = '9d5ba1737b748d23d1c647a29527dee1'


# In[80]:


# Define the job to search
WHAT = 'data%20analyst'


# In[81]:


# File to store results
csv_file = 'top_companies.csv'


# In[82]:


url = f'https://api.adzuna.com/v1/api/jobs/ca/top_companies?app_id={APP_ID}&app_key={APP_KEY}&what={WHAT}'


# In[83]:


# Make the API request
response = requests.get(url)


# In[84]:


response.status_code


# In[86]:


if response.status_code == 200:
    data = response.json()
    # Parse JSON and extract the leaderboard data
    leaderboard = data['leaderboard']
    # Convert leaderboard data to a DataFrame
    df = pd.DataFrame(leaderboard)
    # Save the DataFrame to a CSV file
    output_file = "Top_Companies.csv"
    df.to_csv(output_file, index=False)
    print(f"Data saved to {output_file}")
    # plot the data in bar chart
    if not df.empty and 'canonical_name' in df and 'count' in df:
        plt.figure(figsize=(10, 6))
        bars = plt.barh(df['canonical_name'], df['count'], color='skyblue')

        # Add labels and title
        plt.xlabel('Count', fontsize=12)
        plt.ylabel('Company Name', fontsize=12)
        plt.title('Top Companies by Count of Job Vacancy (data analyst) - valide at 2024-12-10 12:55', fontsize=14)
        plt.gca().invert_yaxis()  # Invert the Y-axis for better visualization
        
        # Add data labels next to each bar
        for bar in bars:
            width = bar.get_width()
            plt.text(width + 0.2, bar.get_y() + bar.get_height()/2, str(int(width)), 
                     va='center', ha='left', fontsize=10, color='black')

        # Show the plot
        plt.tight_layout()
        plt.show()
    else:
        print("DataFrame is empty or required columns are missing.")
else:
    print("DATA WAS NOT EXTRACTED, ERROR CODE: " & response.status_code)


# In[ ]:




