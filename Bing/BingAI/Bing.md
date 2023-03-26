# **Bing, Hi!**

Use a keyword detection system to identify when the user wants to draw something.
For example, if the user says “draw me a cat”, the keyword is “draw” and the image content is “a cat”.
The Bing Chat then uses an image generation model to produce a picture of a cat and display it in the chat.
The image generation model is trained on a large dataset of images and captions, and can create realistic and diverse images for different requests.
The code for this project is written in Python.


## Buzzword Detection
This repository contains code for detecting buzzwords in a given sentence.

## Usage
The main function is detect_buzz_words, which takes a sentence and a list of buzzwords as input and returns a list of detected buzzwords.

```
from buzzword_detection import detect_buzz_words

sentence = "draw an elephant"
buzz_words = ["draw"]
detected_buzz_words = detect_buzz_words(sentence, buzz_words)
print(detected_buzz_words)

```

## How it works
The detect_buzz_words function works by looping through each buzzword and checking if it appears in the sentence. To do this, it uses the get_similarity function to calculate the similarity between each word in the sentence and the current buzzword. If the similarity is greater than 0.7, the buzzword is considered to be detected and is added to the list of detected buzzwords.

The get_similarity function calculates the similarity between two strings by converting them to vectors using the text_to_vector function and then calculating the cosine similarity between the vectors using the get_cosine function.


# contact me
for anything. you can contact me via <ins> **[mail](https://mail.google.com/mail/u/0/?fs=1&tf=cm&source=mailto&su=Bing%20AI%20Feedback&Code&to=ronniri2010@gmail.com&body=)**. </ins>
