jointly_owned_business_premise = 14000
jointly_owned_business_hypothesis = 64000

# the hypothesis refers to the amount of money in the business, which is also mentioned in the premise
if jointly_owned_business_hypothesis <= jointly_owned_business_premise:
    # check if the hypothesis value contradicts the estimate of 'jointly_owned_business_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money in the business
    # any amount of money less than 'jointly_owned_business_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
