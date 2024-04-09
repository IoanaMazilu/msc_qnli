premise_amount = 57
hypothesis_amount = 57

# the premise and hypothesis mention the amount of global debt growth since the financial crisis
if premise_amount == hypothesis_amount:
    # check if the amount of global debt growth in the hypothesis contradicts the amount of growth in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
