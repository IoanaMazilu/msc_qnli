premise_saving_amount = 100
hypothesis_saving_amount = 80

# the hypothesis refers to the percentage of decrease in the saving amount
if hypothesis_saving_amount < premise_saving_amount * 0.3:
    # check if the hypothesis value contradicts the estimate of 30% decrease in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of decrease
    # any percentage of decrease less than 30% is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
