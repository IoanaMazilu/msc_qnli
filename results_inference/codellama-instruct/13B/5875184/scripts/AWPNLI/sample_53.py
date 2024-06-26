premise_lambs = 6048.0
premise_white_lambs = 193.0
hypothesis_black_lambs = 5854.0

# the hypothesis refers to the number of black lambs, which are also mentioned in the premise
# compute the total number of lambs in the premise
total_lambs_premise = premise_lambs + premise_white_lambs
if hypothesis_black_lambs > total_lambs_premise:
    # check if the number of black lambs in the hypothesis contradicts the number of lambs from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
