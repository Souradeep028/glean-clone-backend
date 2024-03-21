import os
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone
import requests


API_KEY = os.getenv('PINECONE_API_KEY')
owner = os.getenv("OWNER")

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
pc = Pinecone(api_key=API_KEY)

index = pc.Index("github-repos")


def generate_embeddings(texts):
    return model.encode(texts, show_progress_bar=True)


def get_repo_link(repo_name):
    base_url = f"https://api.github.com/repos/{owner}/{repo_name}"

    response = requests.get(base_url)

    if response.status_code == 200:
        data = response.json()
        repo_details = {
            'html_url': data.get('html_url'),
            'ssh_url': data.get('ssh_url'),
            'visibility': 'public' if data.get('private') == False else 'private',
            'created_at': data.get('created_at'),
            'languages': []
        }

        languages_response = requests.get(f"{base_url}/languages")
        if languages_response.status_code == 200:
            languages_data = languages_response.json()
            repo_details['languages'] = list(languages_data.keys())
        else:
            repo_details['languages'] = ['Error fetching languages']

        return repo_details
    else:
        return {'error': 'Failed to retrieve repository information'}


def query(query_text):
    query_embedding = generate_embeddings(query_text).tolist()
    matches = index.query(vector=query_embedding, top_k=5,
                          include_metadata=True)['matches']

    results = []
    for match in matches:
        repo_name = match['metadata']['repo']
        file_name = match['metadata']['file_name']
        file_path = match['metadata']['file_path']
        score = match['score']
        repo_details = get_repo_link(repo_name)
        html_url = repo_details.get('html_url')

        result = {
            'file_name': file_name,
            'file_url': f"{html_url}/tree/main/{file_path}",
            'repository': repo_name,
            'repo_link': html_url,
            'ssh_url': repo_details.get('ssh_url'),
            'languages_used': repo_details.get('languages'),
            'owner': owner,
            'visibility': repo_details.get('visibility'),
            'created_at': repo_details.get('created_at'),
            'relevance': f"{score * 100:.1f}%"
        }
        results.append(result)
    return results
