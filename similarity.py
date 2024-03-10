from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np
import psycopg2
import numpy as np
import pgvector
from pgvector.psycopg2 import register_vector
from psycopg2.extensions import adapt, register_adapter
 
n_value=int(input())
conn = psycopg2.connect(
    host="aws-0-ap-southeast-1.pooler.supabase.com",
    database="postgres",
    user="postgres.vaojqdupdbepdqahwrok",
    password="Shanmugam@1"
)
cur = conn.cursor()

# Register the vector type with psycopg2
register_vector(conn)

cur.execute("SELECT embedding FROM embeddings WHERE id = %s", (n_value,))
vector_data = cur.fetchone()
cur.execute("SELECT id FROM embeddings ORDER BY embedding <-> (%s) LIMIT 5 ",(np.array(vector_data)))
result=cur.fetchall()
print(result)
conn.commit()
cur.close()
conn.close()  

# Use the concatenated embeddings as features
# For example, you can concatenate the embeddings along axis 1 to create a single feature vector for each sample
# concatenated_embeddings = np.concatenate(embeddings)
# print(len(concatenated_embeddings))
# print("Shape of concatenated embeddings:", concatenated_embeddings.shape)