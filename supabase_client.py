from supabase import create_client
import os

def get_supabase_client():
    return create_client ('https://eqwifrsvkqnugdaxqtbm.supabase.co', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVxd2lmcnN2a3FudWdkYXhxdGJtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTgxMTk0NjUsImV4cCI6MjAzMzY5NTQ2NX0.m_5NIJtqdyxOFhTVhVd5BeVVQRqAuI42lrGWBdUOheA')

def fetch_articles():
    client = get_supabase_client()
    response = client.table("articles").select("*").execute()
    return response.data

def update_tags(article_id, tags):
    client = get_supabase_client()
    data = {
        "tag_1": tags[0],
        "tag_2":tags[1],
        "tag_3" :tags[2]
    }
    print(data)
    response = client.table("articles").update(data).eq('id', article_id).execute()
    
    if response and response.data:
        return response.data
    else:
        print("No data found or an error occurred.")
        return None



# if __name__ == "__main__":
#     fetch_articles()