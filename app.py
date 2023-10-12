# Import necessary libraries
import streamlit as st
import PyPDF2
from models.sentiment_analysis import perform_sentiment_analysis
from models.information_extraction import perform_information_extraction

def extract_text_from_pdf(uploaded_file):
    if uploaded_file is not None:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
        return text
    return None

def main():
    st.title("Text Mining Web App")

    st.sidebar.header("Select a Text Mining Task")

    task = st.sidebar.selectbox("Select a Text Mining Task", ("Sentiment Analysis", "Information Extraction", "Text Classification", "Text Clustering"))

    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    # Add a "Submit" button to trigger text mining tasks
    if st.sidebar.button("Submit"):
        if uploaded_file is not None:
            # Create a loader
            with st.spinner("Performing the task..."):
                # Extract text from the uploaded PDF file
                file_text = extract_text_from_pdf(uploaded_file)

                if file_text:
                    st.write("PDF Text Content:")
                    st.text(file_text)
                else:
                    st.write("Text extraction failed. Please upload a valid PDF file.")

                # Continue with the selected text mining task
                if task == "Sentiment Analysis":

                    sentiment = perform_sentiment_analysis(file_text)
                    if sentiment == "Positive":
                        st.success("Sentiment: Positive")
                    elif sentiment == "Negative":
                        st.error("Sentiment: Negative")
                    else:
                        st.warning("Sentiment: Neutral")

                if task == "Information Extraction":
                    st.write("Performing Information Extraction...")

                    named_entities = perform_information_extraction(file_text)

                    if named_entities:
                        st.write("Named Entities:")
                        data = {"Entity": [entity for entity, _ in named_entities], "Label": [label for _, label in named_entities]}
                        st.table(data)
                    else:
                        st.write("No named entities found.")

                elif task == "Text Classification":
                    st.write("Performing Text Classification...")
                elif task == "Text Clustering":
                    st.write("Performing Text Clustering...")


if __name__ == '__main__':
    main()
