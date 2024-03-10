from sklearn.preprocessing import LabelEncoder
import pandas as pd
df = pd.read_csv(r"C:\Users\Admin\harini\PeerLink (1).csv") 
df1 = df[["Domain", "Category_Area", "Residing_Country", "Professional_Certification", "spoken_language", "gender"]]

columns_to_encode = ["Domain", "Category_Area", "Residing_Country", "Professional_Certification", "spoken_language", "gender"]
label_encoder = LabelEncoder()
encoded_values = {}

for column in columns_to_encode:
    df[column] = label_encoder.fit_transform(df[column])
    encoded_values[column] = dict(zip(label_encoder.classes_, label_encoder.transform(label_encoder.classes_)))

print("Encoded Values:")
for column, values in encoded_values.items():
    print(f"{column}: {values}")