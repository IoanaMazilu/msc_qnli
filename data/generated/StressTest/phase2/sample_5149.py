# Premise: After more than 2 years, Arun's age will be 26 years.
# Hypothesis: After 6 years, Arun's age will be 26 years.
# Golden Label: neutral

future_age_premise = 26
future_age_hypothesis = 26
years_future_premise = 2
years_future_hypothesis = 6

# the hypothesis talks about Arun's future age, referenced also in the premise
if future_age_premise != future_age_hypothesis:
    # check if the future age in the hypothesis contradicts the future age mentioned in the premise
    label = "contradiction"
elif years_future_hypothesis <= years_future_premise:
    # check if the number of years in the future in the hypothesis contradicts the number of years in the future mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years in the future
    # any number of years greater than 'years_future_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

