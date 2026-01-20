import os
from byaldi import RAGMultiModal
from dotenv import load_dotenv

load_dotenv()

class ColPaliIndexer:
    def __init__(self, model_name="vidore/colpali-v1.2"):
        """
        Initializes the Vision Transformer-based RAG model.
        Bypasses traditional OCR to embed document patches directly.
        """
        self.rag = RAGMultiModal.from_pretrained(model_name)
        print(f"Loaded Vision Transformer model: {model_name}")

    def create_index(self, data_path, index_name="enterprise_docs"):
        """
        Indexes a directory of documents. 
        Each page is treated as an image to preserve visual context.
        """
        if not os.path.exists(data_path):
            raise FileNotFoundError(f"Data directory not found: {data_path}")
            
        print(f"Indexing documents in {data_path}...")
        self.rag.index(
            input_path=data_path,
            index_name=index_name,
            store_collection_with_index=True,
            overwrite=True
        )
        print(f"Index '{index_name}' successfully created.")

if __name__ == "__main__":
    # Example usage for your GitHub portfolio
    indexer = ColPaliIndexer()
    indexer.create_index(data_path="./data/sample_reports")
