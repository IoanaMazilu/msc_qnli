num_lambs_premise = 6048.0
num_white_lambs_premise = 193.0
num_black_lambs_hypothesis = 5854.0

# the hypothesis refers to the number of black lambs, which are also mentioned in the premise
# compute the total number of lambs in the premise
total_lambs_premise = num_lambs_premise - num_white_lambs_premise
if num_black_lambs_hypothesis > total_lambs_premise:
    # check if the number of black lambs in the hypothesis contradicts the number of lambs from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
