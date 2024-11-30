# DDS-ElasticSearch - Product Search Engine

This project demonstrates a **fashion product search engine** built with **ElasticSearch** and **Streamlit**. The application uses **vector similarity search** powered by **sentence-transformers** to provide efficient and relevant search results for products in Myntra's catalog.

---

## Features

- **Vector Similarity Search**: Embedding-based search using product descriptions.
- **Streamlit Frontend**: Interactive user interface for query input and result display.
- **ElasticSearch Integration**: Handles data storage and similarity-based querying.
- **Real-Time Results**: Immediate response for user search queries.

---

## Technologies Used

- **Python**: Core programming language.
- **ElasticSearch**: For indexing and querying product data.
- **Sentence-Transformers**: Converts text to embeddings for vector search.
- **Streamlit**: Frontend for user interaction.
- **Pandas**: For data manipulation and preprocessing.

---

## File Structure

```plaintext
.
├── main.py                # Streamlit application
├── indexMapping.py        # ElasticSearch index mapping configuration
├── myntra_products_catalog.csv # Dataset (50000 records)
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
└── index_data.py          # Script to preprocess and upload data to ElasticSearch
```

