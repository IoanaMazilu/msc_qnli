# Define variables for the numerical entities in the premise and hypothesis
loss_indu_premise = 0
loss_indu_hypothesis = 0
time_period_premise = 0
time_period_hypothesis = 0
interest_rate_premise = 0
interest_rate_hypothesis = 0

# Extract all quantities as valid numbers
loss_indu_premise = float(loss_indu_premise)
loss_indu_hypothesis = float(loss_indu_hypothesis)
time_period_premise = int(time_period_premise)
time_period_hypothesis = int(time_period_hypothesis)
interest_rate_premise = float(interest_rate_premise)
interest_rate_hypothesis = float(interest_rate_hypothesis)

# Perform calculations
loss_indu_hypothesis = loss_indu_premise * (1 + interest_rate_premise/100)**time_period_premise
loss_indu_hypothesis = loss_indu_hypothesis * (1 + interest_rate_hypothesis/100)**time_period_hypothesis

# Compare the values
if loss_indu_hypothesis <= loss_indu_premise:
    # The hypothesis value contradicts the premise
    label = "contradiction"
elif time_period_hypothesis < time_period_premise:
    # The hypothesis value is less than the premise
    label = "contradiction"
elif interest_rate_hypothesis < interest_rate_premise:
    # The hypothesis value is less than the premise
    label = "contradiction"
else:
    # The hypothesis value is consistent with the premise
    label = "neutral"

print(label)
