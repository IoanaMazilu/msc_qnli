matthew_rate_premise = 3
johnny_rate_premise = 4
matthew_rate_hypothesis = 8
johnny_rate_hypothesis = 4

# the hypothesis refers to Matthew's and Johnny's walking rates mentioned in the premise
if matthew_rate_premise > matthew_rate_hypothesis:
    # check if 'matthew_rate_premise' contradicts the estimate of less than 'matthew_rate_hypothesis'
    label = "contradiction"
elif johnny_rate_premise != johnny_rate_hypothesis:
    # check if 'johnny_rate_premise' contradicts 'johnny_rate_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
