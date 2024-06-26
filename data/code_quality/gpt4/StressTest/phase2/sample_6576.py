shirts_bought_premise = 160
shirts_bought_hypothesis = 560

# the hypothesis refers to the number of shirts Vijay bought, which is also mentioned in the premise
if shirts_bought_premise >= shirts_bought_hypothesis:
    # check if the number of shirts Vijay bought in the premise contradicts the estimate of less than 'shirts_bought_hypothesis' in the hypothesis
    label = "contradiction"
elif shirts_bought_premise != shirts_bought_hypothesis:
    # check if the number of shirts Vijay bought in the premise contradicts the number of shirts in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
