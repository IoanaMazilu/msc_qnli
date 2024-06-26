saving_amount_premise = 80
saving_amount_hypothesis = 30

# the hypothesis refers to the percentage of saving amount decreased due to loan payment
if saving_amount_hypothesis <= saving_amount_premise:
    # check if the hypothesis value contradicts the estimate of less than'saving_amount_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of saving amount decreased
    # any percentage greater than'saving_amount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
