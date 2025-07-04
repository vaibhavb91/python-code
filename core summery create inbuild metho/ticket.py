import string
from collections import Counter

def read_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def tokenize_sentences(text):
    sentences = text.split('. ')
    return [s.strip() for s in sentences if s]

def tokenize_words(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.lower().split()
    return words

def summarize_text(text, sentence_count=3):
    sentences = tokenize_sentences(text)
    words = tokenize_words(text)

    # Count word frequency
    word_freq = Counter(words)

    # Score sentences
    sentence_scores = {}
    for sent in sentences:
        sent_words = tokenize_words(sent)
        score = sum(word_freq.get(word, 0) for word in sent_words)
        sentence_scores[sent] = score

    # Pick top N sentences
    sorted_sentences = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)
    summary = [sent for sent, score in sorted_sentences[:sentence_count]]

    return ' '.join(summary)

# 📂 Your input file
file_path = 'input.txt'
text = read_text(file_path)
summary = summarize_text(text, sentence_count=3)

print("📌 Summary:\n", summary)
