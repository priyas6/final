from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np
import psycopg2
import numpy as np
import pgvector
from pgvector.psycopg2 import register_vector
# Sample data

df = pd.read_csv(r"C:\Users\Admin\harini\example.csv") 
data = df[["Domain", "Category_Area", "Residing_Country", "Professional_Certification", "spoken_language","Skillset_score"]]

conn = psycopg2.connect(
    host="aws-0-ap-southeast-1.pooler.supabase.com",
    database="postgres",
    user="postgres.vaojqdupdbepdqahwrok",
    password="Shanmugam@1"
)
cur = conn.cursor()

# Register the vector type with psycopg2
register_vector(conn)

# Load SBERT model
sbert_model = SentenceTransformer('distilbert-base-nli-mean-tokens')
conn.commit()
for index, row in data.iterrows():
    text = f"{row['Domain']} {row['Category_Area']}{row['Residing_Country']}  {row['Professional_Certification']}{row['spoken_language']} row{['Skillset_score']}"
    embedding = sbert_model.encode([text]) # Embedding for a single text
    cur.execute("Insert into data_embeddings (embedding) VALUES (%s)",(np.array(embedding)))
    conn.commit()
cur.close()
conn.close()  

# Use the concatenated embeddings as features
# For example, you can concatenate the embeddings along axis 1 to create a single feature vector for each sample
# concatenated_embeddings = np.concatenate(embeddings)
# print(len(concatenated_embeddings))
# print("Shape of concatenated embeddings:", concatenated_embeddings.shape)