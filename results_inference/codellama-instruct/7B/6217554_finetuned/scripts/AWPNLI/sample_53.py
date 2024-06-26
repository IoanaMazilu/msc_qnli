lambs_premise = 6048.0
black_lambs_premise = 193.0
total_lambs_hypothesis = 5854.0

# the hypothesis talks about the number of black lambs, which are also referenced in the premise
# compute the total number of black lambs from the premise
total_black_lambs_premise = lambs_premise - black_lambs_premise
if total_black_lambs_hypothesis!= total_black_lambs_premise:
    # check if the number of black lambs from the hypothesis contradicts the number of black lambs from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
    
print(label)
