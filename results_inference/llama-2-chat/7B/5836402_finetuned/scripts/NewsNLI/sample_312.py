scores_premise = [4, 4, 1, 1]
scores_hypothesis = [4, 4, 1, 1]

# the hypothesis mentions the score of the match between Arsenal and Galatasaray, which is also referenced in the premise
# however, the hypothesis refers to the player who scored the hat-trick, which cannot be entailed from the premise
label = "neutral"

print(label)
