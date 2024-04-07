# Premise: He will be 5/3 times as old as Tom 6 years hence.
# Hypothesis: He will be more than 3/3 times as old as Tom 6 years hence.
# Golden Label: entailment

old_ratio_premise = 5/3
old_ratio_hypothesis = 3/3

# the hypothesis refers to the age ratio of 'he' and 'Tom' in the future, which is also mentioned in the premise
if old_ratio_hypothesis >= old_ratio_premise:
    # check if the ratio in the hypothesis contradicts the age ratio in the premise
    label = "contradiction"
elif old_ratio_hypothesis < old_ratio_premise:
    # if the hypothesis ratio is less than the premise ratio, it can be explicitly entailed from the premise
    label = "entailment"

print(label)

