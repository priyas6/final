import streamlit as st
import pandas as pd
import partner as pr
import fitz
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def main():
    
   # st.title("Find your Collaborative Partner")

    # uploaded_pdf = st.file_uploader("Upload your Resume: ", type=['pdf'])
        text = ""

    #if uploaded_pdf is not None:
        
        # Convert pdf data to text
        doc = fitz.open(stream=uploaded_pdf.read(), filetype="pdf")
        for page in doc:
            text += str(page.get_text())
        # st.write(text) 
        doc.close()

        # Find user's skillset
        skillset = pr.find_skillset(text)
        # st.write(skillset)

        # Display user skillset as wordcloud
        word_cloud = WordCloud(collocations = False, background_color = 'white').generate(skillset)
        plt.imshow(word_cloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

        # Find skillset score for all users
        # Display closest user's skillset as wordcloud
        similar_user_skillset = pr.find_skillset_score(skillset)
        word_cloud = WordCloud(collocations = False, background_color = 'white').generate(similar_user_skillset)
        plt.imshow(word_cloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

    # Input section
    # Extra user data may be from these columns -- Residing_Country, Professional_Certification, spoken_language
    name               = st.text_input("Name", "Enter your name here")
    gender             = st.selectbox('Gender',('Male', 'Female'))    
    mail               = st.text_input("Mail ID", "Enter your Mail Id here")
    lang               = st.selectbox('Primary Spoken Language',('English', 'German', 'Korean', 'Japanese'))    
    age                = int(st.number_input('Age'))

    Domain             = st.selectbox(
                        'Domain of Interest',
                        ('DATA SCIENCE', 'HR', 'ARTS', 'WEB DESIGNING',
                        'MECHANICAL ENGINEER', 'HEALTH AND FITNESS', 'CIVIL ENGINEER',
                        'JAVA DEVELOPER', 'BUSINESS ANALYST', 'SAP DEVELOPER',
                        'AUTOMATION TESTING', 'ELECTRICAL ENGINEERING',
                        'OPERATIONS MANAGER', 'PYTHON DEVELOPER', 'DEVOPS ENGINEER',
                        'NETWORK SECURITY ENGINEER', 'PMO', 'DATABASE', 'HADOOP',
                        'ETL DEVELOPER', 'DOTNET DEVELOPER', 'BLOCKCHAIN', 'TESTING',
                        'DESIGNER', 'INFORMATION-TECHNOLOGY', 'BUSINESS-DEVELOPMENT',
                        'HEALTHCARE', 'FITNESS', 'AGRICULTURE', 'BPO', 'CONSULTANT',
                        'DIGITAL-MEDIA', 'AUTOMOBILE', 'ENGINEERING', 'CONSTRUCTION',
                        'BANKING'))

    Category_area       = st.selectbox(
                        'Category Area',
                        ('Tech', 'Others'))

    Residing_Country    = st.selectbox(
                        'Residing Country',
                        ('Australia', 'China', 'France', 'Germany', 'Greece', 'India', 'Italy', 'Japan', 'Korea', 
                        'New Zealand', 'Spain', 'Singapore', 'United Kingdom', 'United States'))

    yoe                = int(st.number_input('Years of Experience'))

    github             = int(st.number_input('Github score'))
    linkedin           = int(st.number_input('LinkedIn score'))
    kaggle             = int(st.number_input('Kaggle score'))

    Professional_Certification    = st.selectbox(
                            'Professional Certification',
                            ('Microsoft Certified: Azure Data Scientist Associate',
                            'Google Professional Data Engineer',
                            'AWS Certified Data Analytics - Specialty',
                            'SPHR (Senior Professional in Human Resources)',
                            'SHRM-CP (Society for Human Resource Management Certified Professional)',
                            'PHR (Professional in Human Resources)',
                            'Certified Graphic Designer (CGD)',
                            'Autodesk Certified Professional', 'Adobe Certified Expert',
                            'AWS Certified Solutions Architect - Associate',
                            'Microsoft Certified: Azure Fundamentals',
                            'Google Associate Cloud Engineer', 'Cambridge English',
                            'LEED Accredited Professional (LEED AP)',
                            'Professional Engineer (PE) License',
                            'Certified Construction Manager (CCM)',
                            'Certified Professional Constructor (CPC)',
                            'Project Management Professional (PMP)',
                            'Spring Professional Certification',
                            'Java EE Enterprise Architect Certification',
                            'Oracle Certified Professional, Java SE 11 Developer',
                            'Oracle Certified Associate, Java SE 8 Programmer',
                            'Java EE Web Component Developer Certification',
                            'SAP Certified Application Associate - SAP HANA',
                            'SAP Certified Technology Associate - System Administration (SAP HANA as a Database)',
                            'SAP Certified Development Associate - SAP Fiori Application Developer',
                            'SAP Certified Development Associate - ABAP with SAP NetWeaver',
                            'ISTQB Certified Tester Advanced Level - Test Automation Engineer',
                            'HP Certified Professional - UFT/QTP',
                            'Selenium Certification (Selenium WebDriver)',
                            'ISTQB Certified Tester Foundation Level',
                            'Google Cloud Certified - Professional Data Engineer',
                            'MongoDB Certified DBA Associate',
                            'MySQL Database Administrator Certification',
                            'Oracle Database SQL Certification',
                            'Microsoft Certified: Azure Database Administrator Associate',
                            'EMC Data Science Associate (EMCDSA)',
                            'Hortonworks Certified Associate (HCA) Administrator',
                            'Microsoft Certified: Azure Data Engineer Associate',
                            'Cloudera Certified Associate (CCA) Administrator',
                            'MapR Certified Hadoop Developer',
                            'Certified Corda Developer (CCD)',
                            'Certified Ethereum Developer (CED)',
                            'Certified Blockchain Expert (CBE)',
                            'Certified Blockchain Architect (CBA)',
                            'Certified Blockchain Developer (CBD)',
                            'Microsoft Certified: Azure Administrator Associate',
                            'Certified Information Systems Security Professional (CISSP)',
                            'Cisco Certified Network Associate (CCNA)', 'CompTIA A+',
                            'HubSpot Content Marketing Certification',
                            'Google Certified Professional - Digital Marketing',
                            'Adobe Certified Expert - Photoshop',
                            'Facebook Blueprint Certification',
                            'Hootsuite Social Marketing Certification'))

    hackathon          = int(st.number_input('Hackathons count'))
    coding             = int(st.number_input('Coding problems count'))
    articles           = int(st.number_input('Articles published count'))
    projects           = int(st.number_input('No. of Projects done in the specified domain'))
    papers             = int(st.number_input('Papers published'))
    patents            = int(st.number_input('Patents count'))

    # Convert input to df and send it to backend to find the numerical data score
    data={"years_of_experience": yoe, "kaggle_score": kaggle, "no_of_projects": projects, 
    "coding_problems_count": coding, "hackathons_count": hackathon, "github_score": github, 
    "age": age, "linked_score": linkedin,  "articles_published_count": articles, 
    "papers_published_count": papers, "patents_count": patents}
    input_df = pd.DataFrame(data, index=[0])
    st.write(pr.find_numerical_data_score(input_df))

    
if __name__ == "__main__":
    main()