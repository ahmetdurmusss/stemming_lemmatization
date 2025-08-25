# NLP Stemming & Lemmatization

Simple Python module for text stemming and lemmatization using NLTK.

## Installation

```bash
pip install nltk
```

## Usage

```python
from stemming_lemmatization import stem_word, lemmatize_word, compare_stem_lemma

# Single word processing
stem_word("running")      # "run"
lemmatize_word("running", pos='v')  # "run"

# Compare methods
words = ["running", "better", "went"]
results = compare_stem_lemma(words)
```

## Functions

- `stem_word(word)` - Returns stem of a word
- `lemmatize_word(word, pos='n')` - Returns lemma of a word
- `stem_words(words)` - Process word list
- `lemmatize_words(words, pos='n')` - Process word list
- `compare_stem_lemma(words)` - Compare both methods

## License

MIT

## Author
- LinkedIn: (https://www.linkedin.com/in/ahmet-durmus-6b67b72b6/)