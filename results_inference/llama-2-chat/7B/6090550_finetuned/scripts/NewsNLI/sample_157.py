 score_premise = 3
score_hypothesis = 3

# the hypothesis mentions the number of goals West Ham scored in the second half, which is also mentioned in the premise
if score_hypothesis!= score_premise:
    # check if the number of goals in the hypothesis contradicts the number of goals in the premise
    label = "contradiction"
else:
    # if the number of goals in the hypothesis does not contradict the number of goals in the premise, we can infer entailment
    label = "entailment"

print(label)
