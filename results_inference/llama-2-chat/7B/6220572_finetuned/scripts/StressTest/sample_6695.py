after_premise = 8
after_hypothesis = 8
withdraws_premise = 14000
withdraws_hypothesis = 14000

# the hypothesis refers to the number of months and the amount withdrawn mentioned in the premise
if after_hypothesis!= after_premise:
    # check if the number of months in the hypothesis contradicts the number of months reported in the premise
    label = "contradiction"
elif withdraws_hypothesis!= withdraws_premise:
    # check if the amount withdrawn in the hypothesis contradicts the amount withdrawn reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
