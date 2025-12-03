from textblob import TextBlob
import wikipedia

def search_wikipedia(name):
    """Search Wikipedia for a given name and return a summary."""
    print(f"Searching Wikipedia for: {name}")
    return wikipedia.search(name)

def summarize_wikipedia(name, sentences=3):
    """Get a summary from Wikipedia for a given name."""
    print(f"Getting summary from Wikipedia for name: {name}")
    return wikipedia.summary(name)

def get_text_blob(text):
    """Getting Text Blob object and returns"""
    blob = TextBlob(text)
    return blob

def get_phrases(name):
    """Find wikipedia name and return noun phrases."""
    summary = summarize_wikipedia(name)
    blob = get_text_blob(summary)
    phrases = blob.noun_phrases
    return phrases