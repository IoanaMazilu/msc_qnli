 score_premise = 2
score_hypothesis = 5

# the hypothesis refers to the score Jerry must earn on the fourth test to raise his average by a certain number of points, as mentioned in the premise
if score_hypothesis!= score_premise:
    # check if the score in the hypothesis contradicts the score in the premise
    label = "contradiction"
else:
    # if the scores in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
