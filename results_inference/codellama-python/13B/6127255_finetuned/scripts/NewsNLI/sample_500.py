sevilla_score_premise = 3
zaragoza_score_premise = 1
sevilla_score_hypothesis = 3
zaragoza_score_hypothesis = 1

# the hypothesis mentions the final score of the game, which is also mentioned in the premise
# however, the hypothesis refers to Sevilla's position in the La Liga, which cannot be entailed from the premise
label = "neutral"

print(label)
