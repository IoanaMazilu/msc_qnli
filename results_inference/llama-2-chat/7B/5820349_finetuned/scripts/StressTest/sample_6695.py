amount_premise = 14000
amount_hypothesis = 14000
months_premise = 8
months_hypothesis = 8

# the hypothesis refers to the amount and time period mentioned in the premise
if amount_hypothesis >= amount_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif months_hypothesis!= months_premise:
    # check if the time period in the hypothesis contradicts the time period reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
