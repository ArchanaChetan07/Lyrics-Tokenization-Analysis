# Group Comparison: Lyrics Tokenization & Analysis

This repository contains an NLP project aimed at comparing two different groups of text data using various tokenization techniques and visualization tools. The main notebook, `Group Comparison.ipynb`, performs exploratory data analysis (EDA), text preprocessing, and visualizations to identify differences between two datasets.

##  Contents

- `Group Comparison.ipynb` — Main analysis notebook
- `requirements.txt` — List of Python packages to run the notebook
- `data/` — Directory for storing input data (add your datasets here)
- `images/` — Generated visualizations (word clouds, bar plots, etc.)


## Features

- Text cleaning and tokenization
- Stopword and punctuation removal
- Emoji extraction and frequency analysis
- Frequency distribution of top tokens
- Word cloud generation for visual comparison
- Descriptive statistical summary of token use

##  Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YourUsername/Group-Comparison.git
cd Group-Comparison
```

### 2. Create a virtual environment

```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Launch Jupyter Notebook

```bash
jupyter notebook Group\ Comparison.ipynb
```

## Technologies Used

- Python
- Jupyter Notebook
- NLTK
- Matplotlib / Wordcloud
- Regex
- Collections
