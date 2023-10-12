# Text Mining Web App

![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)

A web application for performing various text mining tasks on uploaded PDF files. This application allows users to extract text from PDFs and perform sentiment analysis, information extraction, text classification, and text clustering tasks.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Tasks](#tasks)
  - [Sentiment Analysis](#sentiment-analysis)
  - [Information Extraction](#information-extraction)
  - [Text Classification](#text-classification)
  - [Text Clustering](#text-clustering)
- [Contributing](#contributing)
- [License](#license)

## Features

- Upload PDF files for text mining.
- Extract text from PDFs.
- Perform sentiment analysis using the VADER sentiment analyzer.
- Extract named entities from text using spaCy.
- Perform text classification and text clustering tasks.
- Interactive and user-friendly interface using Streamlit.

## Getting Started

### Prerequisites

- Python 3.6+
- Pip (Python package manager)

### Installation

1. Clone the repository:

   ```sh
   git clone git@github.com:0aaryan/text_mining_streamlit.git
   ```

2. Navigate to the project directory:

   ```sh
   cd text-mining-web-app
   ```

3. Create a virtual environment (optional but recommended):

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. Install the required dependencies:

   ```sh
   pip install -r requirements.txt
   ```

## Usage

To run the web application, execute the following command:

```sh
streamlit run app.py
```

This will start the app, and you can access it through your web browser at `http://localhost:8501`.

## Tasks

### Sentiment Analysis

Sentiment analysis is performed using the VADER sentiment analyzer from NLTK. It analyzes the sentiment of the provided text and categorizes it as "Positive," "Negative," or "Neutral."

### Information Extraction

Information extraction utilizes the spaCy library with the `en_core_web_sm` model to extract named entities (entities like organizations, locations, dates, etc.) from the text.

### Text Classification

Text classification allows users to perform text classification tasks on the provided text. You can integrate your custom text classification model here.

### Text Clustering

Text clustering allows users to perform text clustering tasks. The app uses the TF-IDF vectorizer and K-Means clustering to cluster the text based on the number of clusters provided by the user.

## Contributing

We welcome contributions from the community. If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

You can customize this README by adding more sections or details specific to your project. Make sure to update the GitHub repository with the README file, and it will be displayed prominently on the repository's main page.
