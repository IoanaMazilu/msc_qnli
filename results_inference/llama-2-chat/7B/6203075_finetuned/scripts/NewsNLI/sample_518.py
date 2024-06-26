score_premise = 2
score_hypothesis = 2

# the hypothesis mentions the score of the Bayern Munich vs. Hannover game, which is also mentioned in the premise
if score_hypothesis!= score_premise:
    # check if the score in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
else:
    # if the scores in the hypothesis and premise match, we can infer entailment
    label = "entailment"

print(label)
