years_future_premise = 6
age_future_premise = 26
years_future_hypothesis = 6
age_future_hypothesis = 26

# the hypothesis refers to the same future age of Arun, but with a different number of years in the future
if age_future_hypothesis != age_future_premise:
    # check if the predicted future age contradicts the one from the premise
    label = "contradiction"
elif years_future_hypothesis >= years_future_premise:
    # check if the number of years in the future when Arun will be 'age_future_hypothesis' contradicts the premise
    label = "contradiction"
else:
    # the premise gives an exact number of years in the future when Arun will be 'age_future_premise'
    # a lesser number of years until Arun becomes 'age_future_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
