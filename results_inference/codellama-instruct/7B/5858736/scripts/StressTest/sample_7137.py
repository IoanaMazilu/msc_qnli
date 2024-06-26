saving_amount_premise = 10
saving_amount_hypothesis = 60

# the hypothesis refers to the percentage of saving amount decreased due to loan payment and current balance
if saving_amount_hypothesis >= saving_amount_premise:
    # check if the hypothesis value contradicts the percentage of saving amount decreased in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of saving amount decreased
    # any percentage less than'saving_amount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
