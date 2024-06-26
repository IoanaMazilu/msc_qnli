years_future_premise = 15
years_future_hypothesis = 85
multiplier = 5
years_past = 5

# The hypothesis refers to Suresh's age in the future and in the past, 
# which are also referenced in the premise.
if years_future_hypothesis >= years_future_premise:
    # Check if the hypothesis value contradicts the premise's future age estimate
    label = "contradiction"
elif years_future_hypothesis < (multiplier * years_past):
    # Check if the hypothesis future age estimate contradicts the premise's future age estimate
    label = "contradiction"
else:
    # The premise gives only an estimate for Suresh's future age
    # Any future age less than 'years_future_hypothesis' is consistent with the premise, 
    # but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
