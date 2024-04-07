# Premise: After more than 2 years, Arun's age will be 32 years.
# Hypothesis: After 4 years, Arun's age will be 32 years.
# Golden Label: neutral

arun_future_age_premise = 32
arun_future_years_premise = 2
arun_future_age_hypothesis = 32
arun_future_years_hypothesis = 4

# The hypothesis refers to Arun's age after a certain number of years, which is also mentioned in the premise
if arun_future_age_hypothesis != arun_future_age_premise:
    # Check if the future age of Arun in the hypothesis contradicts the future age mentioned in the premise
    label = "contradiction"
elif arun_future_years_hypothesis <= arun_future_years_premise:
    # Check if the number of years in the future when Arun will reach the age mentioned in the hypothesis contradicts the number of years mentioned in the premise
    label = "contradiction"
else:
    # The premise gives an estimate for the number of years in the future when Arun will be 'arun_future_age_premise' years old
    # Any number of years greater than 'arun_future_years_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

