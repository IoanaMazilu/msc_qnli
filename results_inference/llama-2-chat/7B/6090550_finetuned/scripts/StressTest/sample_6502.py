matthew_rate_premise = 5
matthew_rate_hypothesis = 3
johnny_rate_premise = 4
johnny_rate_hypothesis = 4

# the hypothesis talks about the walking rates of Matthew and Johnny
if matthew_rate_premise >= matthew_rate_hypothesis:
    # check if the hypothesis value contradicts the estimate of less than'matthew_rate_premise'
    label = "contradiction"
elif johnny_rate_premise!= johnny_rate_hypothesis:
    # check if the walking rate of Johnny in the hypothesis contradicts the walking rate of Johnny in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for Matthew's walking rate
    # any walking rate for Matthew that is consistent with the premise is entailed by the hypothesis
    label = "entailment"

print(label)
