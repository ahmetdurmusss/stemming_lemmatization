"""
Kök ve Gövde Analizi - Basit NLP Modülü  
=======================================

Stemming ve Lemmatization için basit fonksiyonlar.

Gereksinimler:
    pip install nltk
"""

import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

# NLTK verilerini indir
try:
    nltk.download('wordnet', quiet=True)
    nltk.download('omw-1.4', quiet=True)
except:
    pass

# Global nesneler
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()


def stem_word(word):
    """Kelimenin kökünü bulur (stemming)"""
    return stemmer.stem(word.lower())


def stem_words(words):
    """Kelime listesinin köklerini bulur"""
    return [stem_word(word) for word in words]


def lemmatize_word(word, pos='n'):
    """
    Kelimenin lemmasını bulur
    
    pos: 'n' (noun), 'v' (verb), 'a' (adjective), 'r' (adverb)
    """
    return lemmatizer.lemmatize(word.lower(), pos)


def lemmatize_words(words, pos='n'):
    """Kelime listesinin lemmalarını bulur"""
    return [lemmatize_word(word, pos) for word in words]


def compare_stem_lemma(words):
    """Stemming ve lemmatization sonuçlarını karşılaştırır"""
    results = {}
    for word in words:
        results[word] = {
            'stem': stem_word(word),
            'lemma': lemmatize_word(word)
        }
    return results


# Örnek kullanım
if __name__ == "__main__":
    test_words = ["running", "runner", "ran", "runs", "better", "going", "went"]
    
    print("Orijinal kelimeler:", test_words)
    print("Stemming sonuçları:", stem_words(test_words))
    print("Lemmatization sonuçları:", lemmatize_words(test_words))
    
    print("\nKarşılaştırma:")
    comparison = compare_stem_lemma(test_words)
    for word, results in comparison.items():
        print(f"{word} -> Stem: {results['stem']}, Lemma: {results['lemma']}")