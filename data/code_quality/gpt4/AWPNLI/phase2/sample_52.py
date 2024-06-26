total_lambs_premise = 6048.0
white_lambs_premise = 193.0
black_lambs_hypothesis = 5855.0

# the hypothesis refers to the number of black lambs, which can be inferred from the premise
# compute the number of black lambs in the premise
black_lambs_premise = total_lambs_premise - white_lambs_premise
if black_lambs_hypothesis != black_lambs_premise:
    # check if the number of black lambs in the hypothesis contradicts the number of black lambs from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
