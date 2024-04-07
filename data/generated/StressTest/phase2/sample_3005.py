# Premise: After 2 years, Arun's age will be 26 years.
# Hypothesis: After more than 2 years, Arun's age will be 26 years.
# Golden Label: contradiction

years_until_age_premise = 2
years_until_age_hypothesis = 2
age_after_years_premise = 26
age_after_years_hypothesis = 26

# the hypothesis refers to the same future age and time period mentioned in the premise
if years_until_age_hypothesis <= years_until_age_premise:
    # check if the hypothesis' estimate of 'more than years_until_age_hypothesis' contradicts the exact period mentioned in the premise
    label = "contradiction"
elif age_after_years_hypothesis != age_after_years_premise:
    # check if the future age in the hypothesis contradicts the future age stated in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

