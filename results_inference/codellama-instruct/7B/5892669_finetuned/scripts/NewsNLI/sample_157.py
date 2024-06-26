score_premise = 3
score_hypothesis = 3

# the hypothesis mentions the score of the game, which is also referenced in the premise
# however, the hypothesis refers to the score at the end of the second half, while the premise mentions the score at halftime
# this is a contradiction, as the premise does not mention any second-half goals
label = "contradiction"

print(label)
