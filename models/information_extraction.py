# import spacy.cli
# import spacy

# # Check if the spaCy model is already installed
# if not spacy.util.is_package("en_core_web_sm"):
#     # If not installed, download it
#     spacy.cli.download("en_core_web_sm")

# # Load the spaCy model
# nlp = spacy.load("en_core_web_sm")

# def perform_information_extraction(text):
#     # Process the text with spaCy
#     doc = nlp(text)

#     # Extract and return named entities
#     named_entities = [(entity.text, entity.label_) for entity in doc.ents]
#     return named_entities

# # Example usage
# if __name__ == "__main__":
#     example_text = "Apple Inc. is headquartered in Cupertino, California."
#     named_entities = perform_information_extraction(example_text)
#     for entity, label in named_entities:
#         print(f"{entity} ({label})")
