# Premise: After 6 years, Arun's age will be 26 years.
# Hypothesis: After more than 1 years, Arun's age will be 26 years.
# Golden Label: entailment

years_to_age_premise = 6
age_premise = 26
years_to_age_hypothesis = 1
age_hypothesis = 26

# the hypothesis refers to the age of Arun and the number of years until that age mentioned in the premise
if age_premise != age_hypothesis:
    # check if the age in the hypothesis contradicts the age mentioned in the premise
    label = "contradiction"
elif years_to_age_hypothesis >= years_to_age_premise:
    # check if the number of years in the hypothesis contradicts the number of years reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

