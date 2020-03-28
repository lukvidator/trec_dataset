from bs4 import BeautifulSoup
import html as ihtml
import re
import string



PUNCTUATION_MAPPING = dict.fromkeys(map(ord, string.punctuation), " ")


def remove_html(text):
    # Getting plain text
    # TODO: parser lxml or default?
    text = BeautifulSoup(ihtml.unescape(text), "lxml").get_text()
    # Removing HTML comments
    text = re.sub(r"(<!--.*?-->)", "", text, flags=re.DOTALL)
    
    return text


def remove_hyperlinks(text):
    # Removing hyperlinks
    return re.sub(r"http[s]?://\S+", "", text)


def map_punctuation_to_space(text, mapping=None):
    if mapping is None:
        mapping = PUNCTUATION_MAPPING
        
    return text.translate(mapping)


def regularize_spacing(text):
    return re.sub(r"\s+", " ", text)


def clean_text(text):
    """
    Clean text from HTML tags, hyperlinks and HTML comments.
    Remove punctuation. Regularize spacings.
    """
    
    text = remove_html(text)
    text = remove_hyperlinks(text)
    text = map_punctuation_to_space(text)
    text = regularize_spacing(text)
    # TODO: text.strip
    # TODO: stopwords
    
    return text.lower()

