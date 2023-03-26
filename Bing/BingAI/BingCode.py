from collections import Counter
import re, math

def detect_buzz_words(sentence: str, buzz_words):
    # Encode the sentence using the Universal Sentence Encoder model
    # embeddings = model([sentence])

    # Loop through each buzzword and check if it appears in the sentence
    detected = []
    for buzz_word in buzz_words:
        # buzz_word_embedding = model([buzz_word])
        for word in sentence.split(" "):
            wordStr = word
            # word = model([word])
            # if((wordStr == ("start" or "run") )and buzz_word == "open"):
            # print("test me")
            similarity = get_similarity(wordStr, buzz_word)
            if similarity > 0.7:
                detected.append(buzz_word)
                break

    if len(detected) > 0:
        return detected

    # If none of the buzzwords appear in the sentence, return None
    return []

WORD = re.compile(r'\w+')

def get_cosine(vec1, vec2):
    # print vec1, vec2
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])
    sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
    sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

def text_to_vector(text):
    return Counter(WORD.findall(text))

def get_similarity(a, b):
    a = text_to_vector(a.strip().lower())
    b = text_to_vector(b.strip().lower())
    return get_cosine(a, b)


# Example usage of detect_buzz_words function
sentence = "draw an elephant"
buzz_words = ["draw"]
detected_buzz_words = detect_buzz_words(sentence, buzz_words)
print(detected_buzz_words)
x = location_of_buzz = sentence.split(" ").index(" ".join(detected_buzz_words))
list_of_words = sentence.split(" ")
buzzword = " ".join(detected_buzz_words)
for word in buzz_words:
    if word in list_of_words:
        list_of_words.remove(word)
tobingai = " ".join(list_of_words)
print(tobingai) # instad of printing it, move it to your image AI in your way (you can do it with API of some kind.)
exit()
