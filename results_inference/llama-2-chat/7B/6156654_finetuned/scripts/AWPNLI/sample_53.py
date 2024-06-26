lambs_total = 6048.0
white_lambs = 193.0
black_lambs = 5854.0

# the hypothesis refers to the number of black lambs, which can be calculated from the premise
# compute the number of black lambs in the premise
black_lambs_premise = lambs_total - black_lambs
if black_lambs_premise!= black_lambs:
    # check if the number of black lambs in the hypothesis contradicts the number of black lambs in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
