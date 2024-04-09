denomination_premise = 50
denomination_hypothesis = 70

# the hypothesis talks about the denomination of bonds, referenced also in the premise
if denomination_hypothesis <= denomination_premise:
    # check if the hypothesis value contradicts the estimate of less than 'denomination_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the denomination, any denomination greater than 'denomination_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
