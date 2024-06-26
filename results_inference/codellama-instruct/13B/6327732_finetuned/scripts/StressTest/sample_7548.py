saving_amount_premise = 30
saving_amount_hypothesis = 80

# the hypothesis refers to the percentage of decrease in the saving amount
if saving_amount_hypothesis >= saving_amount_premise:
    # check if the hypothesis value contradicts the percentage of decrease in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the percentage of decrease
    # any percentage of decrease less than'saving_amount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
