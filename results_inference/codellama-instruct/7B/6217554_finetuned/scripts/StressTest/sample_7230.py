purchased_wheat_premise = 30
purchased_wheat_hypothesis = 40

if purchased_wheat_hypothesis <= purchased_wheat_premise:
    # check if the hypothesis value contradicts the number of purchased wheat in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of purchased wheat
    # any number of wheat greater than 'purchased_wheat_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
