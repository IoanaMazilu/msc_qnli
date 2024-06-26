deposit_premise = 62500
deposit_hypothesis = 62500
percent_return_premise = 8
percent_return_hypothesis = 8

# the hypothesis refers to the amount deposited and the annual return percentage mentioned in the premise
if deposit_hypothesis >= deposit_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif percent_return_hypothesis != percent_return_premise:
    # check if the annual return percentage in the hypothesis contradicts the percentage mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
