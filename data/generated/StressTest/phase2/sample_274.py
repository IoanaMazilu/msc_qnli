# Premise: After more than 1 years, Arun's age will be 26 years.
# Hypothesis: After 6 years, Arun's age will be 26 years.
# Golden Label: neutral

arun_future_age_premise = 26
years_after_premise = 1
arun_future_age_hypothesis = 26
years_after_hypothesis = 6

# the hypothesis refers to Arun's future age, as stated in the premise
if arun_future_age_hypothesis != arun_future_age_premise:
    # check if the future age of Arun in the hypothesis contradicts the future age reported in the premise
    label = "contradiction"
elif years_after_hypothesis <= years_after_premise:
    # check if the years after which the age is calculated in the hypothesis contradicts the years mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only a lower limit for the number of years after which Arun's age will be 'arun_future_age_premise'
    # any number of years greater than 'years_after_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

