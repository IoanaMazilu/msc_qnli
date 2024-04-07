# Premise: After 6 years, Arun's age will be 26 years.
# Hypothesis: After more than 5 years, Arun's age will be 26 years.
# Golden Label: entailment

years_future_premise = 6
years_future_hypothesis = 5
age_future_premise = 26
age_future_hypothesis = 26

# the hypothesis refers to the age of Arun after a number of years, mentioned in the premise
if years_future_hypothesis >= years_future_premise:
    # check if the number of years in the hypothesis contradicts the number of years in the premise
    label = "contradiction"
elif age_future_hypothesis != age_future_premise:
    # check if the age in the hypothesis contradicts the age in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

