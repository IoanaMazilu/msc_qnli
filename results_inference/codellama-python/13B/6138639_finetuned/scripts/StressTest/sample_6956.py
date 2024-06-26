average_shirts_premise = 40
average_shirts_hypothesis = 40
shirts_purchased = 8

# the hypothesis refers to the average number of shirts with Salman, Ambani and Dalmiya mentioned in the premise
if average_shirts_hypothesis >= average_shirts_premise:
    # check if the estimate of 'average_shirts_hypothesis' contradicts the average number of shirts in the premise
    label = "contradiction"
elif (average_shirts_premise - shirts_purchased) <= average_shirts_hypothesis:
    # check if the average number of shirts in the hypothesis contradicts the average number of shirts after purchase in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
