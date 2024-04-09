ana_premise = 2
ana_hypothesis = 8

# the hypothesis refers to the number of P Ana goes before, which is also mentioned in the premise
if ana_hypothesis <= ana_premise:
    # check if the number of P Ana goes before in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of P Ana goes before
    # any number of P greater than 'ana_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
