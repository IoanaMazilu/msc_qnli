lambs_total = 6048.0
lambs_white = 193.0
lambs_black = 5854.0

# the hypothesis refers to the number of black lambs, which is also mentioned in the premise
if lambs_black!= lambs_total - lambs_white:
    # check if the number of black lambs in the hypothesis contradicts the number of black lambs in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
