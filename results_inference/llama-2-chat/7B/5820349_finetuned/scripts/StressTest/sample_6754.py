goes_premise = 2
goes_hypothesis = 8

# the hypothesis talks about the number of P Ana goes before, referenced also in the premise
if goes_hypothesis <= goes_premise:
    # check if the hypothesis value contradicts the estimate of more than 'goes_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of P Ana goes before
    # any number of P greater than 'goes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
