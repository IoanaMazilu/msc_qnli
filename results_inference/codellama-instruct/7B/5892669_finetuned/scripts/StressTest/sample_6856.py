min_sum_premise = 5
max_sum_premise = 35
min_sum_hypothesis = 1
max_sum_hypothesis = 35

# the hypothesis refers to the same sum range as the premise
if min_sum_hypothesis < min_sum_premise or max_sum_hypothesis > max_sum_premise:
    # check if the sum range in the hypothesis contradicts the sum range in the premise
    label = "contradiction"
else:
    # the premise gives a specific sum range
    # any sum range within this range is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
