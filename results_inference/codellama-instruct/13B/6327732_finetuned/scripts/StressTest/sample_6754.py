ana_goes_before_premise = 2
ana_goes_before_hypothesis = 8

# the hypothesis refers to the number of people that Ana goes before
if ana_goes_before_hypothesis <= ana_goes_before_premise:
    # check if the hypothesis value contradicts the estimate of more than 'ana_goes_before_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people that Ana goes before
    # any number of people greater than 'ana_goes_before_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
