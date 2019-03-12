import string
from collections import Counter
import tqdm
import nltk
import re

if __name__ == "__main__":
    genuine = open("data/genuine.txt").read()
    clickbait = open("data/clickbait.txt").read()
    vocabulary, genuine_preprocessed, clickbait_preprocessed = preprocess_text(genuine, clickbait)
    open("data/vocabulary.txt", "w").write("\n".join(vocabulary))
    open("data/genuine.preprocessed.txt", "w").write("\n".join(genuine))
    open("data/clickbait.preprocessed.txt", "w").write("\n".join(clickbait))