import spacy
from spacy.pipeline import EntityRuler
from spacy.lang.en import English
from spacy.tokens import Doc
from gensim.models.keyedvectors import KeyedVectors
import pandas as pd
import skillset_score as skscore
from scipy.spatial import distance
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
pd.options.mode.chained_assignment = None 

def find_skillset(resume_str):

    nlp = spacy.load('en_core_web_sm')
    skills = "/home/harini/personal/projects/datasets/jz_skill_patterns.jsonl"
    ruler = nlp.add_pipe("entity_ruler", before="ner")
    ruler.from_disk(skills)
    doc = nlp(resume_str)

    skills = []
    str = ","

    for ent in doc.ents:
        if ent.label_ == 'SKILL':
            skills.append(ent.text)
    skills = [i.capitalize() for i in set ([i.lower() for i in skills])]
    return(str.join(skills))

def find_skillset_score(inp_skillset):

    df = pd.read_csv("/home/harini/personal/projects/datasets/Peerlink/PeerLink.csv")
    user_skillsets = []
    for i in range (len(df)):
        user_skillsets.append(str(df['Skillset'][i]))
    scores = skscore.get_most_similar_sentence(str(inp_skillset), user_skillsets)

    df['Skillset_score'] = 0
    for i in range (len(df)):
        df['Skillset_score'][i] = scores[i]

    df.to_csv("/home/harini/personal/projects/datasets/Peerlink/PeerLink.csv", index = False)
    # print("Length=",len(df))
    # print("Length=",len(scores))
    
    most_similar_index = scores.argmax()
    most_similar_sentence = user_skillsets[most_similar_index]
    
    return str(most_similar_sentence)

def find_numerical_data_score(input_df):

    df = pd.read_csv("/home/harini/personal/projects/datasets/Peerlink/PeerLink.csv")
    df1 = df[['years_of_experience', 'kaggle_score', 'no_of_projects',
       'coding_problems_count', 'hackathons_count', 'github_score', 'age',
       'linked_score', 'articles_published_count', 'papers_published_count',
       'patents_count']]

    distances = df1.apply(lambda row: distance.cosine(row, input_df.iloc[0]), axis=1) 
    distance_frame = pd.DataFrame(data={"dist": distances, "idx": distances.index})
    distance_frame.sort_values(by=["dist"], inplace=True)

    for i in range(len(distance_frame)):
        distance_frame['dist'][i] = 1-distance_frame['dist'][i]

    df['NumericalData_Score'] = 0
    for i in range (len(df)):
        df['NumericalData_Score'][i] = distance_frame['dist'][i]

    df.to_csv("/home/harini/personal/projects/datasets/Peerlink/PeerLink.csv", index = False)
    # print("Length=",len(df))
    # print("Length=",len(distance_frame))
    return distance_frame

def main():
    
    # skillset = find_skillset("I am a Java developer")
    # print(find_skillset_score(skillset))
    data={"years_of_experience": 0, "kaggle_score": 0, "no_of_projects": 2, "coding_problems_count": 20, "hackathons_count": 0, "github_score": 7, "age": 19, "linked_score": 2,  "articles_published_count": 4, "papers_published_count": 0, "patents_count": 0}
    input_df = pd.DataFrame(data, index=[0])
    # print(input_df)
    find_numerical_data_score(input_df)

if __name__ == "__main__":
    main()