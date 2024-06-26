matthew_rate_premise = 5
johnny_rate_premise = 4
matthew_rate_hypothesis = 3
johnny_rate_hypothesis = 4

# the hypothesis refers to the walking rates of Matthew and Johnny mentioned in the premise
if matthew_rate_hypothesis >= matthew_rate_premise:
    # check if the walking rate of Matthew in the hypothesis contradicts the estimate of less than'matthew_rate_premise'
    label = "contradiction"
elif johnny_rate_hypothesis!= johnny_rate_premise:
    # check if the walking rate of Johnny in the hypothesis contradicts the walking rate of Johnny reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the walking rate of Matthew
    # any walking rate of Matthew less than'matthew_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
