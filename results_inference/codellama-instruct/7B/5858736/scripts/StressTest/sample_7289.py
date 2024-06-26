business_premise = 14000
business_hypothesis = 24000

# the hypothesis refers to the total value of the business jointly owned by the speaker and James and Greg
if business_hypothesis <= business_premise:
    # check if the estimate of 'business_hypothesis' contradicts the value reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the total value of the business
    # any value greater than 'business_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
