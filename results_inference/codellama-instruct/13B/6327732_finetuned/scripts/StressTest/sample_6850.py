billy_apples_premise = 20
billy_apples_hypothesis = 10

# the hypothesis refers to the number of apples mentioned in the premise
if billy_apples_hypothesis >= billy_apples_premise:
    # check if the hypothesis value contradicts the estimate of less than 'billy_apples_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of apples
    # any number of apples less than 'billy_apples_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
