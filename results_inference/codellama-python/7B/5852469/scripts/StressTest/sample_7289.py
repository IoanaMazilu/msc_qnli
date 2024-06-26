shares_business_premise = 14000
shares_business_hypothesis = 14000

# the hypothesis refers to the number of shares in a business that he jointly owns with two other persons (James and Greg)
if shares_business_hypothesis <= shares_business_premise:
    # check if the estimate of'shares_business_hypothesis' contradicts the number of shares in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of shares
    # any number of shares greater than'shares_business_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
