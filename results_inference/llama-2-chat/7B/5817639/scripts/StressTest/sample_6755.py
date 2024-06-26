ana_goes_premise = 8
ana_goes_hypothesis = 7

# the hypothesis talks about the number of P Ana goes before, referenced also in the premise
if ana_goes_hypothesis <= ana_goes_premise:
    # check if the hypothesis value contradicts the estimate of 'ana_goes_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of P Ana goes before
    # any number of P Ana goes before less than 'ana_goes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
