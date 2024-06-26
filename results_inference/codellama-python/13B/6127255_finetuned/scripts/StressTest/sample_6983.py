borrowed_rate_premise = 6
borrowed_rate_hypothesis = 8

# the hypothesis refers to the borrowing rate mentioned in the premise
if borrowed_rate_hypothesis!= borrowed_rate_premise:
    # check if the borrowing rate in the hypothesis contradicts the borrowing rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
