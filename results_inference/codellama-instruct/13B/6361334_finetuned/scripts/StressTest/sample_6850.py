apples_premise = 20
apples_hypothesis = 10

# the hypothesis refers to the number of apples mentioned in the premise
if apples_hypothesis >= apples_premise:
    # check if the hypothesis value contradicts the estimate of less than 'apples_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of apples
    # any number of apples less than 'apples_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
