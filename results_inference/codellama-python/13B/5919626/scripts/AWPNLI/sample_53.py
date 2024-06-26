# the hypothesis talks about the number of black lambs, which are also referenced in the premise
# find the total number of lambs from the premise 
total_lambs_premise = 6048.0
if 5854.0 >= total_lambs_premise:
    # check if the total lambs from the hypothesis contradict the estimate of less than 'total_lambs_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
    
print(label)
