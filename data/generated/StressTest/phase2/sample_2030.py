# Premise: He will be 5/3 times as old as Tom 6 years hence.
# Hypothesis: He will be 6/3 times as old as Tom 6 years hence.
# Golden Label: contradiction

age_ratio_premise = 5/3
age_ratio_hypothesis = 6/3
time_future = 6

# the hypothesis refers to the age comparison mentioned in the premise
if age_ratio_premise != age_ratio_hypothesis:
    # check if the 'age_ratio_hypothesis' contradicts the 'age_ratio_premise'
    label = "contradiction"
else:
    # if the age ratio in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)

