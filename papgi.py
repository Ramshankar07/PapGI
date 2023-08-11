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
    def get_recent_ml_papers(num_papers=10):
            base_url = "http://export.arxiv.org/api/query?"
            search_query = "cat:cs.LG"  # Category for Machine Learning on arXiv
    
            params = {
                "search_query": search_query,
                "sortBy": "submittedDate",
                "sortOrder": "descending",
                "max_results": num_papers
            }
    
            response = requests.get(base_url, params=params)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                entries = soup.find_all("entry")
                
                papers = []
                for entry in entries:
                    title = entry.title.text.strip()
                    authors = [author.find("name").text.strip() for author in entry.find_all("author")]
                    published = entry.published.text.strip()
                    summary = entry.summary.text.strip()
                    
                    paper_info = {
                        "title": title,
                        "authors": authors,
                        "published": published,
                        "summary": summary
                    }
                    papers.append(paper_info)
                
                return papers
            else:
                print("Error:", response.status_code)
                return None

    # Get 5 recent ML papers
    recent_ml_papers = get_recent_ml_papers(num_papers=5)

    if recent_ml_papers:
    # Save the data in JSON format
        with open("recent_ml_papers.json", "w") as json_file:
            json.dump(recent_ml_papers, json_file, indent=4)

        print("Recent ML papers saved to 'recent_ml_papers.json'")
    else:
        print("Failed to retrieve recent ML papers.")
        pdf_file_path = "file"
    
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
        
            for page_num in range(pdf_reader.numPages):
                page = pdf_reader.getPage(page_num)
                content += page.extract_text()
    
    

    if __name__ == '__main__':
        main()