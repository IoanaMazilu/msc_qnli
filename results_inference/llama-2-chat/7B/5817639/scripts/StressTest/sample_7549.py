saving_amount_premise = float(80)
saving_amount_hypothesis = 30

# the hypothesis talks about the percentage of decrease in saving amount, which is also mentioned in the premise
if saving_amount_hypothesis <= saving_amount_premise:
    # check if the hypothesis value contradicts the estimate of less than'saving_amount_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the percentage of decrease, which is consistent with the hypothesis value
    label = "entailment"

print(label)
