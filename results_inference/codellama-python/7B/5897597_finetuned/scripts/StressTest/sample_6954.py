average_shirts_premise = 40
average_shirts_hypothesis = 80
shirts_purchased = 8

# the hypothesis refers to the average number of shirts with Salman, Ambani and Dalmiya, mentioned in the premise
if average_shirts_premise >= average_shirts_hypothesis:
    # check if the estimate of 'average_shirts_hypothesis' contradicts the average number of shirts in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)