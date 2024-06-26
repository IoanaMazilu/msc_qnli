goals_premise = 3
goals_hypothesis = 3

# the hypothesis mentions the score of the match, which is also mentioned in the premise
if goals_hypothesis!= goals_premise:
    # check if the score in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value and the premise value are the same, we can infer entailment
    label = "entailment"

print(label)
