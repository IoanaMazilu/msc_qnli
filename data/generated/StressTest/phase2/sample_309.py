# Premise: After 6 years, Sandy’s age will be 34 years.
# Hypothesis: After more than 4 years, Sandy’s age will be 34 years.
# Golden Label: entailment

years_premise = 6
years_hypothesis = 4
age_premise = 34
age_hypothesis = 34

# The hypothesis refers to the age of Sandy and the number of years passed, as in the premise
if years_hypothesis >= years_premise and age_hypothesis != age_premise:
    # check if the estimate of 'years_hypothesis' contradicts the number of years in the premise
    # and if the age in the hypothesis contradicts the age in the premise
    label = "contradiction"
elif years_hypothesis < years_premise and age_hypothesis == age_premise:
    # check if the number of years in the hypothesis does not contradict the number of years in the premise
    # and if the age in the hypothesis does not contradict the age in the premise
    label = "entailment"
else:
    # if the hypothesis values do not contradict the premise values, we infer neutrality
    label = "neutral"

print(label)

