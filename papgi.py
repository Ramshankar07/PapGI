import numpy as np
import scipy as sp
import requests
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize
import PyPDF2


def extract_summary(paper):
     # Tokenize the paper into sentences
    sentences = sent_tokenize(paper)
    
    # Calculate the length of each sentence
    sentence_lengths = [len(sentence.split()) for sentence in sentences]
    
    # Calculate the average sentence length
    avg_sentence_length = sum(sentence_lengths) / len(sentence_lengths)
    
    # Find the sentences that are below the average length
    short_sentences = [sentence for sentence in sentences if len(sentence.split()) < avg_sentence_length]
    
    # Join the short sentences to form the summary
    summary = ' '.join(short_sentences)
    
    return summary

def main():
    url = "https://arxiv.org/list/cs/recent"
    response = requests.get(url)
    
    # Create a BeautifulSoup object by parsing the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the element containing the information for the recent paper
    paper_element = soup.find('div', {'class': 'recent-paper'})
    
    # Extract the title and authors from the paper element
    title = paper_element.find('h1').text.strip()
    authors = paper_element.find('div', {'class': 'authors'}).text.strip()
    
    # Extract the abstract from the paper element
    abstract = paper_element.find('div', {'class': 'abstract'}).text.strip()
    
    # Return the scraped information as a dictionary
    paper_info = {
        'title': title,
        'authors': authors,
        'abstract': abstract
    }
    
     content = ""
     pdf_file_path = "file"
    
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            content += page.extract_text()
    
    

if __name__ == '__main__':
    main()