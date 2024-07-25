import fastembed
from qdrant_client import QdrantClient

qdrant_client = QdrantClient(
    url="https://cd5dba88-8077-4aa3-9e35-78fd82a4a850.us-east4-0.gcp.cloud.qdrant.io:6333",
    api_key="9Yt6Xfds2O-84IT8LwFVl3i0Ly8DRFZD7AGr1SrhABJDBF-VqaHZ3g",
)

qdrant_client.add(
    collection_name="user01",
    documents=[
        "Qdrant is a vector database & vector similarity search engine. It deploys as an API service providing search for the nearest high-dimensional vectors. With Qdrant, embeddings or neural network encoders can be turned into full-fledged applications for matching, searching, recommending, and much more!",
        "Docker helps developers build, share, and run applications anywhere — without tedious environment configuration or management.",
        "PyTorch is a machine learning framework based on the Torch library, used for applications such as computer vision and natural language processing.",
        "MySQL is an open-source relational database management system (RDBMS). A relational database organizes data into one or more data tables in which data may be related to each other; these relations help structure the data. SQL is a language that programmers use to create, modify and extract data from the relational database, as well as control user access to the database.",
        "NGINX is a free, open-source, high-performance HTTP server and reverse proxy, as well as an IMAP/POP3 proxy server. NGINX is known for its high performance, stability, rich feature set, simple configuration, and low resource consumption.",
        "FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.",
        "SentenceTransformers is a Python framework for state-of-the-art sentence, text and image embeddings. You can use this framework to compute sentence / text embeddings for more than 100 languages. These embeddings can then be compared e.g. with cosine-similarity to find sentences with a similar meaning. This can be useful for semantic textual similar, semantic search, or paraphrase mining.",
        "The cron command-line utility is a job scheduler on Unix-like operating systems. Users who set up and maintain software environments use cron to schedule jobs (commands or shell scripts), also known as cron jobs, to run periodically at fixed times, dates, or intervals.",
    ]
)
