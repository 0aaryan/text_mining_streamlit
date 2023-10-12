import streamlit as st
import PyPDF2
from models.sentiment_analysis import vader_lexicon, textblob_analysis, bert_analysis

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
    st.write("An app for text mining tasks including sentiment analysis, information extraction, text classification, and text clustering.")

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

            if task == "Sentiment Analysis":
                st.write("Performing Sentiment Analysis...\n")

                # Create separate loaders for each sentiment analysis method
                with st.spinner("Performing Sentiment Analysis using VADER Lexicon..."):
                    vader_sentiment, vader_score = vader_lexicon(file_text)

                with st.spinner("Performing Sentiment Analysis using TextBlob..."):
                    textblob_sentiment, textblob_score = textblob_analysis(file_text)

                with st.spinner("Performing Sentiment Analysis using Transformers BERT..."):
                    bert_sentiment, bert_score = bert_analysis(file_text)

                # Display results
                st.subheader("Sentiment Analysis Results:")
                result_data = {
                    "Method": ["VADER Lexicon", "TextBlob", "Transformers BERT"],
                    "Sentiment": [vader_sentiment, textblob_sentiment, bert_sentiment],
                    "Score (%)": [f"{vader_score:.2f}%", f"{textblob_score:.2f}%", f"{bert_score:.2f}%"]
                }
                result_table = st.table(result_data)

                st.subheader("Sentiment Scores Visualization:")
                chart_data = {
                    "Method": ["VADER Lexicon", "TextBlob", "Transformers BERT"],
                    "Score": [vader_score, textblob_score, bert_score]
                }
                st.bar_chart(chart_data, x="Method", y="Score")

                # Determine the best model
                best_model = max(
                    ("VADER Lexicon", vader_score),
                    ("TextBlob", textblob_score),
                    ("Transformers BERT", bert_score),
                    key=lambda x: x[1]
                )

                st.success(f"Best Model for Sentiment Analysis: {best_model[0]}")


                if task == "Information Extraction":
                    st.write("Performing Information Extraction...")
                elif task == "Text Classification":
                    st.write("Performing Text Classification...")
                elif task == "Text Clustering":
                    st.write("Performing Text Clustering...")


if __name__ == '__main__':
    main()
