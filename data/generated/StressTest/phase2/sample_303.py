# Premise: If twice the age of Sunil is more than Syam's age by 4 years, what is Sunil's age?
# Hypothesis: If twice the age of Sunil is more than Syam's age by more than 2 years, what is Sunil's age?
# Golden Label: entailment

age_difference_premise = 4
age_difference_hypothesis = 2

# The hypothesis refers to the age difference in the premise
if age_difference_hypothesis > age_difference_premise:
    # check if the estimate of 'age_difference_hypothesis' contradicts the age difference in the premise
    label = "contradiction"
elif age_difference_hypothesis < age_difference_premise:
    # any smaller difference than 'age_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

