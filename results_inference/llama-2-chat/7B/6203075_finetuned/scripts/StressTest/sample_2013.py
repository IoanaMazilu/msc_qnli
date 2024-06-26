# Indu's loss due to giving it to Bindu for 2 years at 4% per annum simple interest
indu_loss_2_years = 0.04 * 1000 * 2

# Indu's loss due to giving it to Bindu for less than 6 years at 4% per annum simple interest
indu_loss_less_6_years = 0.04 * 1000 * (6 - 2)

# Hypothesis refers to the same scenario as the premise, but with a different time period
if indu_loss_less_6_years!= indu_loss_2_years:
    # If the loss in the hypothesis is not the same as in the premise, it's a contradiction
    label = "contradiction"
else:
    # If the loss in the hypothesis is the same as in the premise, it's entailment
    label = "entailment"

print(label)
