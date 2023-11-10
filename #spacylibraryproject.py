#spacy library example
import spacy

def extract_keywords(text):
    # Load the English language model
    nlp = spacy.load('en_core_web_sm')

    # Create a Document for kewywords
    doc = nlp(text)

    # Extract keywords
    keywords = [token.text for token in doc if token.is_alpha and not token.is_stop]

    # Remove duplicates and set keywords correctly
    keywords = list(set(keywords))

    return keywords
# Example news article text
news_article =(" With the iPhone 15, Apple aims to further revolutionize the smartphone market. Powered by A15 5nm chip, the device offers a whopping 12K RAM. Users can expect faster charging, 5G connectivity, and advanced machine learning capabilities. Additionally, iPhone 15 maintains Face ID technology for facial recognition and retains a 5.5-inch Retina display for enhanced visual quality. This revolutionary smartphone promises to stay ahead in the competition.")

# Extract keywords from the news article
keywords = extract_keywords(news_article)

# Print the extracted keywords
print("Keywords:", keywords)