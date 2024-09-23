from supabase_client import fetch_articles, update_tags
from generate_tags import generate_tags

def process_articles():
    articles =fetch_articles()
    for article in articles:
        title =article['Title']
        article_id  =article['id']
        tags = generate_tags(title)
        update_tags(article_id, tags)
        print(f"Processed Article ID: {article_id}, Tags: {tags}")


if __name__ == "__main__":
   process_articles()