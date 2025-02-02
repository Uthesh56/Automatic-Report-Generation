# Automatic Report Generator

## Overview

The **Automatic Report Generator** is a Streamlit-based application that allows users to upload product data in various formats (CSV, JSON, or XLSX) and generate detailed reports based on specific queries. The app processes product-related data (such as feedback, ratings, brand, customer demographics, etc.), analyzes it using **Natural Language Processing (NLP)** techniques, and returns relevant insights in the form of a concise, readable report.

### Features:

- **File Upload**: Supports CSV, JSON, and XLSX file formats.
- **Data Processing**: Cleans and preprocesses the data by removing unnecessary words and standardizing text (tokenization, lemmatization, and stop word removal).
- **Product Data Insights**: Analyzes data attributes like feedback, ratings, product categories, customer demographics (age, gender, country), and more.
- **Query-based Reporting**: Users can query specific aspects of the data, including product reviews, ratings, and feedback.
- **Vector Search**: Utilizes **sentence embeddings** and a vector database (ChromaDB) to process queries efficiently.
- **Customizable Reports**: Generates structured reports based on the user’s query.
