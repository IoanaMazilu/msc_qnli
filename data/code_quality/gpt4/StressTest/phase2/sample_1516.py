john_profit_more_than_mike_premise = 400
john_profit_more_than_mike_hypothesis = 800

# the hypothesis refers to the profit John made more than Mike, also mentioned in the premise
if john_profit_more_than_mike_hypothesis <= john_profit_more_than_mike_premise:
    # check if the hypothesis value contradicts the information of 'john_profit_more_than_mike_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the profit John made more than Mike
    # any profit more than 'john_profit_more_than_mike_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
