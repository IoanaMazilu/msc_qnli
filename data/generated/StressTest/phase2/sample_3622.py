# Premise: After more than 2 years, Arun’s age will be 26 years.
# Hypothesis: After 6 years, Arun’s age will be 26 years.
# Golden Label: neutral

years_to_age_premise = 2
years_to_age_hypothesis = 6
arun_future_age_premise = 26
arun_future_age_hypothesis = 26

# the hypothesis refers to the number of years until Arun's age of 26, which is also mentioned in the premise
if arun_future_age_hypothesis != arun_future_age_premise:
    # check if the future age of Arun in the hypothesis contradicts the future age of Arun in the premise
    label = "contradiction"
elif years_to_age_hypothesis <= years_to_age_premise:
    # check if the number of years in the hypothesis contradicts the estimate of more than 'years_to_age_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years until Arun turns 26
    # any number of years greater than 'years_to_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

