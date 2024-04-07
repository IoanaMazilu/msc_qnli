# Premise: After 4 years, Arun's age will be 32 years.
# Hypothesis: After more than 2 years, Arun's age will be 32 years.
# Golden Label: entailment

years_future_premise = 4
arun_age_future_premise = 32
years_future_hypothesis = 2
arun_age_future_hypothesis = 32

# the hypothesis refers to Arun's age in the future, which is also mentioned in the premise
if arun_age_future_hypothesis != arun_age_future_premise:
    # check if the future age of Arun in the hypothesis contradicts the future age mentioned in the premise
    label = "contradiction"
elif years_future_hypothesis >= years_future_premise:
    # check if the number of years in the future in the hypothesis contradicts the number of years in the future mentioned in the premise
    label = "contradiction"
else:
    # the premise gives a specific time frame and age for Arun, any time less than 'years_future_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
