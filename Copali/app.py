import streamlit as st
from retriever import ColPaliRetriever
from PIL import Image
import base64
from io import BytesIO

st.set_page_config(page_title="ColPali Vision RAG", layout="wide")
st.title("📄 Multimodal Document Intelligence")
st.subheader("Powered by ColPali Vision Transformers")

# Initialize Retriever
@st.cache_resource
def get_retriever():
    return ColPaliRetriever()

try:
    retriever = get_retriever()
    
    query = st.text_input("Ask a question about your documents (e.g., charts, tables, text):")

    if query:
        with st.spinner("Searching visual embeddings..."):
            results = retriever.search(query)
            
            cols = st.columns(len(results))
            for i, res in enumerate(results):
                with cols[i]:
                    st.write(f"**Score: {res.score:.4f}**")
                    # Display the retrieved page image
                    img = Image.open(BytesIO(base64.b64decode(res.base64_image)))
                    st.image(img, caption=f"Page {res.page_num}", use_container_width=True)

except Exception as e:
    st.error(f"Error: {e}. Please ensure you have indexed documents first.")
