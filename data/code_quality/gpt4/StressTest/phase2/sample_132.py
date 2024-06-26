# Define the premise variables
john_future_age_factor_premise = 2
time_future_years_premise = 4

# Define the hypothesis variables
john_future_age_factor_hypothesis = 6
time_future_years_hypothesis = 4

# The hypothesis refers to John's age in relation to Tom's age in a future time, also mentioned in the premise
if john_future_age_factor_hypothesis <= john_future_age_factor_premise:
    # Check if the factor of John's future age in relation to Tom's age in the hypothesis contradicts the factor in the premise
    label = "contradiction"
elif time_future_years_hypothesis != time_future_years_premise:
    # Check if the time in the future mentioned in the hypothesis contradicts the time in the future mentioned in the premise
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
