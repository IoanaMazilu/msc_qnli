saving_amount_premise = 30
saving_amount_hypothesis = 80

# the hypothesis refers to the percentage of saving amount decreased due to loan payment
# the premise mentions a decrease in saving amount, but does not specify the percentage
if saving_amount_hypothesis >= saving_amount_premise:
    # check if the hypothesis value contradicts the percentage of saving amount decrease in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of saving amount decrease
    # any percentage less than'saving_amount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
