average_shirts_premise = 40
average_shirts_hypothesis = 40
purchased_shirts_premise = 8
purchased_shirts_hypothesis = 8

# the hypothesis refers to the number of shirts with Salman, Ambani and Dalmiya mentioned in the premise
if average_shirts_hypothesis >= average_shirts_premise:
    # check if the estimate of 'average_shirts_hypothesis' contradicts the number of shirts in the premise
    label = "contradiction"
elif purchased_shirts_hypothesis!= purchased_shirts_premise:
    # check if the number of purchased shirts in the hypothesis contradicts the number of purchased shirts reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
