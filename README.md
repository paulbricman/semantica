# Semantic Knowledge Engine

This project consists of an algorithm which can compute semantic expressions. A semantic expression is a finite combination of arithmetic operators and operands, where most operands are natural words.

Examples of semantic expressions:
```
King - man + woman ≈ Queen

Russian - Russia + China ≈ Chineese

humans + unity ≈ peaceful_coexistence

god - human + earth ≈ heavens

slower - slow + fast ≈ faster

Paris - France + Romania ≈ Bucharest
```

The algorithm delivers intuitive results based on the meaning of used words and arithmetic operators.

## How does it work?
The algorithm has two main components: the interpretation of the mathematical expression contained in a string, and the transformation of words into computable vectors.

The interpretation of the mathematical expression consists of generating an Abstract Syntax Tree from the string and computing its result.

The transformation of words into computable vectors is based on the Word2Vec model, which learns a mapping from a word to its context by generating an intermediary embedding, which is used as its representation in vector space.

Combining the two components we obtain an algorithm which can compute semantic expressions.

![](https://github.com/paubric/python-semantica/blob/master/word2vec2.png)

## Setup
```
python3 -m pip install gensim
```
## Usage
```
python3 semantica.py
[*] Model loaded
human+unity
['peaceful_coexistence', 'human_beings', 'humankind', 'oneness', 'mankind']
```
Wait for the model to load then enter a semantic expression. The algorithm will print the best results.
