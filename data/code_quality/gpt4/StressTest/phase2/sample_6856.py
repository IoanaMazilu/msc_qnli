min_sum_premise = 5
max_sum_premise = 35
min_sum_hypothesis = 1
max_sum_hypothesis = 35

# the hypothesis talks about the number of different sums Matt can make, referenced also in the premise
if min_sum_hypothesis < min_sum_premise or max_sum_hypothesis != max_sum_premise:
    # check if the range of sums in the hypothesis contradicts the range in the premise
    label = "contradiction"
else:
    # the premise gives only the range of sums Matt can make
    # the same range in the hypothesis is consistent with the premise, leading to entailment
    label = "entailment"

print(label)
