future_age_premise = 26
future_years_premise = 6
future_years_hypothesis = 2

# The hypothesis refers to Arun's age in a certain number of years, which is also mentioned in the premise
if future_years_hypothesis >= future_years_premise:
    # Check if the number of future years in the hypothesis contradicts the premise
    label = "contradiction"
elif future_age_premise != future_age_premise:
    # Check if the future age in the hypothesis contradicts the future age mentioned in the premise
    label = "contradiction"
else:
    # The premise gives an exact year and age in the future
    # The hypothesis gives a lower bound for the number of years and the same future age, it is consistent with the premise but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
