business_money_premise = 14000
business_money_hypothesis = 64000

if business_money_premise >= business_money_hypothesis:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money in the business
    # any amount of money less than 'business_money_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
