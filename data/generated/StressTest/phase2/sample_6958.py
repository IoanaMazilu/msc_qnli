# Premise: Venkat purchased twenty dozens of toys at the rate of more than 275 per dozen.
# Hypothesis: Venkat purchased twenty dozens of toys at the rate of 375 per dozen.
# Golden Label: neutral

toys_purchased_premise = 20
toys_purchased_hypothesis = 20
rate_per_dozen_premise = 275
rate_per_dozen_hypothesis = 375

# the hypothesis talks about the number of toys purchased and the rate per dozen, referenced also in the premise
if toys_purchased_hypothesis != toys_purchased_premise:
    # check if the number of toys purchased in the hypothesis contradicts the number mentioned in the premise
    label = "contradiction"
elif rate_per_dozen_hypothesis <= rate_per_dozen_premise:
    # check if the rate per dozen in the hypothesis contradicts the estimate of more than 'rate_per_dozen_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the rate per dozen
    # any rate per dozen greater than 'rate_per_dozen_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

