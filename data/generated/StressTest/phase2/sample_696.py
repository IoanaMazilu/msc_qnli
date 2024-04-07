# Premise: He will be 5/3 times as old as Tom 6 years hence.
# Hypothesis: He will be more than 1/3 times as old as Tom 6 years hence.
# Golden Label: entailment

age_ratio_premise = 5/3
age_ratio_hypothesis = 1/3
future_years = 6

# the hypothesis refers to the age relation between 'he' and Tom mentioned in the premise
if age_ratio_hypothesis >= age_ratio_premise:
    # check if the estimate of 'age_ratio_hypothesis' contradicts the age ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

