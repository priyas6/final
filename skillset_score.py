import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

# Download NLTK resources
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# Load the file containing sentences
def load_sentences(file_path):
   with open(file_path, 'r') as file:
    sentences = file.readlines()
   return [sentence.strip() for sentence in sentences]

# Preprocess the input sentence
def preprocess_sentence(sentence):
   # Tokenize
   tokens = word_tokenize(sentence.lower())
   
   # Remove stopwords
   stop_words = set(stopwords.words('english'))
   tokens = [token for token in tokens if token not in stop_words]
   
   # Lemmatize
   lemmatizer = WordNetLemmatizer()
   tokens = [lemmatizer.lemmatize(token) for token in tokens]
   
   return ' '.join(tokens)

# Get the most similar sentence
def get_most_similar_sentence(user_input, sentences):
   # Preprocess input sentence
   preprocessed_user_input = preprocess_sentence(user_input)
   
   # Preprocess sentences
   preprocessed_sentences = [preprocess_sentence(sentence) for sentence in sentences]
   
   # Create TF-IDF vectorizer
   vectorizer = TfidfVectorizer()
   
   # Generate TF-IDF matrix
   tfidf_matrix = vectorizer.fit_transform([preprocessed_user_input] + preprocessed_sentences)
   
   # Calculate similarity scores
   similarity_scores = (tfidf_matrix * tfidf_matrix.T).A[0][1:]
   print(similarity_scores)
   
   # Find the index of the most similar sentence
   most_similar_index = similarity_scores.argmax()
   most_similar_sentence = sentences[most_similar_index]
   
   print(most_similar_sentence)
   return similarity_scores

# Main program
def main():
   file_path = 'sentences.txt'  # Path to the file containing sentences
   sentences = load_sentences(file_path)
   
   user_input = 'Emotion,Libraries,Python,Languages,Computer science,Flask,Git,User interface,Java,C,Mongodb,Engineering,Database,Ubuntu,Css,Docker,Pandas' 
   get_most_similar_sentence(user_input, sentences)
   # most_similar_sentence = get_most_similar_sentence(user_input, sentences)
   # print('Most similar sentence:', most_similar_sentence)

if __name__ == '__main__':
   main()