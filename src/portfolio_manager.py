import pandas as pd
import chromadb
import uuid
from pathlib import Path

class PortfolioManager:
    def __init__(self, file_path="resources/portfolio.csv"):
        self.file_path = Path(file_path)
        self.data = pd.read_csv(self.file_path)
        self._initialize_vector_store()
        
    def _initialize_vector_store(self):
        """Initialize ChromaDB client and collection"""
        self.chroma_client = chromadb.PersistentClient('vectorstore')
        self.collection = self.chroma_client.get_or_create_collection(
            name="portfolio"
        )

    def load_portfolio(self):
        """Load portfolio data into vector store if not already loaded"""
        if not self.collection.count():
            for _, row in self.data.iterrows():
                self.collection.add(
                    documents=row["Techstack"],
                    metadatas={"links": row["Links"]},
                    ids=[str(uuid.uuid4())]
                )

    def query_links(self, skills, num_results=2):
        """Query relevant portfolio links based on required skills"""
        try:
            results = self.collection.query(
                query_texts=skills,
                n_results=num_results
            )
            return results.get('metadatas', [])
        except Exception as e:
            print(f"Error querying portfolio links: {e}")
            return []