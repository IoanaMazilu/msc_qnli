# Premise: Panjali walked for less than 8 days.
# Hypothesis: Panjali walked for 3 days.
# Golden Label: neutral

walked_days_premise = 8
walked_days_hypothesis = 3

# the hypothesis refers to the number of days Panjali walked, also mentioned in the premise
if walked_days_hypothesis >= walked_days_premise:
    # check if the hypothesis value contradicts the estimate of less than 'walked_days_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days
    # any number of days less than 'walked_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

