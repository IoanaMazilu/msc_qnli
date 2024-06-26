less_than_64000_premise = 64000
jointly_owned_business_hypothesis = 14000

# the hypothesis refers to the amount of money in a business jointly owned by the speaker and two others
if jointly_owned_business_hypothesis <= less_than_64000_premise:
    # check if the hypothesis value contradicts the estimate of less than 'less_than_64000_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money in the business
    # any amount of money less than or equal to 14000 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
