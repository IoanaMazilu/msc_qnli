total_lambs = 6048.0
white_lambs = 193.0
black_lambs_hypothesis = 5854.0

# the hypothesis refers to the number of black lambs, which is also mentioned in the premise
# compute the number of black lambs in the premise
black_lambs_premise = total_lambs - white_lambs
if black_lambs_hypothesis!= black_lambs_premise:
    # check if the number of black lambs in the hypothesis contradicts the number of black lambs in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
