matthew_rate_premise = 3
matthew_rate_hypothesis = 3
johnny_rate_premise = 4
johnny_rate_hypothesis = 4

# the hypothesis refers to Matthew's and Johnny's walking rates mentioned in the premise
if matthew_rate_hypothesis <= matthew_rate_premise:
    # check if 'matthew_rate_hypothesis' contradicts 'matthew_rate_premise'
    label = "contradiction"
elif johnny_rate_hypothesis != johnny_rate_premise:
    # check if 'johnny_rate_hypothesis' contradicts 'johnny_rate_premise'
    label = "contradiction"
else:
    # if the rates in the hypothesis do not contradict the rates in the premise, we can infer entailment
    label = "entailment"

print(label)
