# Can Large Language Models Ace Tic-Tac-Toe?
Naively, language models are unable to play tic tac toe robustly. This is for two reasons:
1. Lack of goal-orientation or understanding of opponent's motivation
2. Hallucinations or factual errors about a given board.

This repo aims to find whether it is possible to decompose the act of playing tic tac toe into smaller tasks such taht we can clear a model more robust to these errors.