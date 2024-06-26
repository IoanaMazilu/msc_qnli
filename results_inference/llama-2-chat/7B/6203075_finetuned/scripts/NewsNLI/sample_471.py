score_premise = 5
score_hypothesis = 5

# the hypothesis mentions the score of the match, which is also mentioned in the premise
if score_hypothesis!= score_premise:
    # check if the score in the hypothesis contradicts the score in the premise
    label = "contradiction"
else:
    # if the scores are the same, it's an entailment
    label = "entailment"

print(label)
