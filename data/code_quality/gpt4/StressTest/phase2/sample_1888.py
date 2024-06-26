matthew_rate_premise = 4
matthew_rate_hypothesis = 3
johnny_rate_premise = 4
johnny_rate_hypothesis = 4

# the hypothesis refers to the walking rates of Matthew and Johnny, also mentioned in the premise
if matthew_rate_hypothesis >= matthew_rate_premise:
    # check if the hypothesis value contradicts the estimate of less than 'matthew_rate_premise'
    label = "contradiction"
elif johnny_rate_hypothesis != johnny_rate_premise:
    # check if the walking rate of Johnny in the hypothesis contradicts the walking rate of Johnny mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
