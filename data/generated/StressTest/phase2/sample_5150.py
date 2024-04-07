# Premise: After 6 years, Arun's age will be 26 years.
# Hypothesis: After 2 years, Arun's age will be 26 years.
# Golden Label: contradiction

future_age_premise = 26
future_years_premise = 6
future_age_hypothesis = 26
future_years_hypothesis = 2

# the hypothesis talks about Arun's future age and the time until that age is reached, both referenced in the premise
if future_age_premise != future_age_hypothesis:
    # check if the future age in the hypothesis contradicts the future age mentioned in the premise
    label = "contradiction"
elif future_years_premise < future_years_hypothesis:
    # check if the number of years until the future age in the hypothesis contradicts the number of years mentioned in the premise
    label = "contradiction"
else:
    # the premise gives a specific future age for Arun after a certain number of years
    # a shorter time until the same future age contradicts the premise
    label = "contradiction"

print(label)

