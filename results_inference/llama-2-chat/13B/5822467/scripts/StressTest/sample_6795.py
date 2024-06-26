# define variables with representative names for the numerical entities in both inputs
lucy_deposit_premise = 62500
lucy_deposit_hypothesis = more_than_22500
interest_rate_premise = 8
interest_rate_hypothesis = 8

# extract all quantities as valid numbers (integers or floats)
lucy_deposit_premise = float(lucy_deposit_premise)
lucy_deposit_hypothesis = float(lucy_deposit_hypothesis)
interest_rate_premise = float(interest_rate_premise)
interest_rate_hypothesis = float(interest_rate_hypothesis)

# compare the variables
if lucy_deposit_hypothesis > lucy_deposit_premise:
    # the hypothesis contradicts the premise
    label = "contradiction"
elif lucy_deposit_hypothesis == lucy_deposit_premise:
    # the hypothesis is neutral with respect to the premise
    label = "neutral"
else:
    # the hypothesis entails the premise
    label = "entailment"

print(label)
