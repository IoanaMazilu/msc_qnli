ana_goes_before_premise = 8
ana_goes_before_hypothesis = 8

# the hypothesis refers to the time Ana goes before, which is also mentioned in the premise
if ana_goes_before_hypothesis >= ana_goes_before_premise:
    # check if the hypothesis value contradicts the estimate of less than 'ana_goes_before_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time Ana goes before
    # any time less than 'ana_goes_before_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
