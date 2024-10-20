import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download('punkt')
nltk.download('stopwords')

def read_text_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None


file_path = 'input.txt' 


text = read_text_from_file(file_path)
if text is None:
    exit()

# tokenize words and remove common stopwords like 'the', 'is', etc.
stop_words = set(stopwords.words("english"))
words = word_tokenize(text.lower())  # Convert all words to lowercase for consistency

# create a frequency table of non-stopword tokens
freq_table = {}
for word in words:
    if word not in stop_words:
        freq_table[word] = freq_table.get(word, 0) + 1

# tokenize the text into sentences for scoring
sentences = sent_tokenize(text)
sentence_scores = {}

# score sentences based on word frequencies
for sentence in sentences:
    for word, freq in freq_table.items():
        if word in sentence.lower():
            sentence_scores[sentence] = sentence_scores.get(sentence, 0) + freq

# calculate the average sentence score to filter significant sentences
if sentence_scores:
    avg_score = sum(sentence_scores.values()) / len(sentence_scores)
else:
    avg_score = 0

# generate a summary by including sentences with a score above a threshold
summary = ' '.join([sentence for sentence in sentences if sentence_scores.get(sentence, 0) > 1.2 * avg_score])


print("\nSummary:")
print(summary if summary else "No significant summary could be generated.")
