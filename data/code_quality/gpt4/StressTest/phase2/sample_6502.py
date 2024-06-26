matthew_rate_premise = 5
matthew_rate_hypothesis = 3
johnny_rate_premise = 4
johnny_rate_hypothesis = 4

# Both the hypothesis and premise refer to the walking rates of Matthew and Johnny
if matthew_rate_hypothesis >= matthew_rate_premise:
    # check if the rate in the hypothesis contradicts the premise that Matthew's rate was less than 'matthew_rate_premise'
    label = "contradiction"
elif johnny_rate_hypothesis != johnny_rate_premise:
    # check if the Johnny's rate in the hypothesis contradicts the Johnny's rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
