# Premise: After 5 years, Arun's age will be 40 years.
# Hypothesis: After less than 5 years, Arun's age will be 40 years.
# Golden Label: contradiction

years_future_premise = 5
years_future_hypothesis = 5
future_age_premise = 40
future_age_hypothesis = 40

# The hypothesis talks about Arun's age in the future, referenced also in the premise
if future_age_hypothesis != future_age_premise:
    # Check if the future age in the hypothesis contradicts the future age mentioned in the premise
    label = "contradiction"
elif years_future_hypothesis >= years_future_premise:
    # Check if the number of years in the future in the hypothesis contradicts the number of years in the premise
    label = "contradiction"
else:
    # The premise gives an exact number of years and age, any lesser number of years is consistent with the premise,
    # but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

