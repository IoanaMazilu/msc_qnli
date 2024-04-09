score_premise = 0
score_hypothesis = 3

# the hypothesis mentions the number of goals scored by West Ham in the second half, which is not mentioned in the premise
if score_hypothesis!= score_premise:
    # check if the number of goals scored in the hypothesis contradicts the number of goals scored in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
