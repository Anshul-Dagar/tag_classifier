from keybert import KeyBERT

kw_model = KeyBERT()

def generate_tags( title:str):
    try:
        keywords =kw_model.extract_keywords(
            title,
            keyphrase_ngram_range=(1,1),
            stop_words='english',
            top_n=3
        )
        tags=[keyword[0].capitalize() for keyword in keywords]
        return tags if len(tags)==3 else tags +["N/A"] * (3-len(tags))
    except Exception as e:
        print(f"Error generating tags: {str(e)}")
        return ["NULL", "NULL", "NULL"]
    
# if __name__ == "__main__":
#     generate_tags(llm_client, 'Linus Torvalds explains why aging Linux developers are a good thing')