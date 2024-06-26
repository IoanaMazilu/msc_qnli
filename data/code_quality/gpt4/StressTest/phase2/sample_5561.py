john_tip_premise = 15
john_tip_hypothesis = 65

# the hypothesis refers to the amount of tip John paid over the original price of the dish
if john_tip_hypothesis <= john_tip_premise:
    # check if the hypothesis value contradicts the estimate of 'john_tip_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of tip John paid
    # any tip greater than 'john_tip_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
