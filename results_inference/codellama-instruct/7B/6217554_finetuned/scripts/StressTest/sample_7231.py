purchased_wheat_premise = 40
purchased_wheat_hypothesis = 30

if purchased_wheat_hypothesis >= purchased_wheat_premise:
    # check if the number of purchased wheat in the hypothesis contradicts the estimate of less than 'purchased_wheat_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of wheat
    # any number of wheat less than 'purchased_wheat_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
