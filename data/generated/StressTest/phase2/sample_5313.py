# Premise: Sandy is younger than Molly by 20 years.
# Hypothesis: Sandy is younger than Molly by less than 30 years.
# Golden Label: entailment

age_difference_premise = 20
age_difference_hypothesis = 30

# the hypothesis refers to the age difference between Sandy and Molly mentioned in the premise
if age_difference_hypothesis < age_difference_premise:
    # check if the estimate of 'age_difference_hypothesis' contradicts the age difference in the premise
    label = "contradiction"
elif age_difference_hypothesis > age_difference_premise:
    # any age difference less than 'age_difference_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

