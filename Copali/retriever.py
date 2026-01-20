import os
from byaldi import RAGMultiModal

class ColPaliRetriever:
    def __init__(self, index_name="enterprise_docs"):
        """
        Loads the multi-vector index for real-time retrieval.
        """
        index_path = os.path.join(".byaldi", index_name)
        if not os.path.exists(index_path):
            raise ValueError(f"Index not found at {index_path}. Run indexer.py first.")
            
        self.rag = RAGMultiModal.from_index(index_name)

    def search(self, query, k=3):
        """
        Performs MaxSim late interaction search.
        Aligns query text tokens with visual document patches.
        """
        results = self.rag.search(query, k=k)
        return results

if __name__ == "__main__":
    # Test search functionality
    retriever = ColPaliRetriever()
    query = "What is the projected revenue growth for Q4?"
    search_results = retriever.search(query)
    
    for i, res in enumerate(search_results):
        print(f"Top {i+1} Result - Page: {res.page_num}, Score: {res.score:.4f}")
