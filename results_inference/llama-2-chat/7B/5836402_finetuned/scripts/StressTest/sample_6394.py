oil_requirement_premise = 7
oil_requirement_hypothesis = 8

# the hypothesis talks about the oil requirement for each cylinder in George's car, referenced also in the premise
if oil_requirement_hypothesis <= oil_requirement_premise:
    # check if the hypothesis value contradicts the estimate of more than 'oil_requirement_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the oil requirement
    # any oil requirement greater than 'oil_requirement_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
