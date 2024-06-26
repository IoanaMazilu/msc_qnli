average_shirts_premise = 70
average_shirts_hypothesis = 60
additional_shirts = 6

# the hypothesis refers to the average number of shirts with Salman, Ambani and Dalmiya mentioned in the premise
if average_shirts_hypothesis >= average_shirts_premise:
    # check if the average number of shirts in the hypothesis contradicts the estimate of less than 'average_shirts_premise' in the premise
    label = "contradiction"
elif average_shirts_hypothesis + additional_shirts != average_shirts_premise + additional_shirts:
    # check if the number of shirts after purchasing in the hypothesis contradicts the number of shirts after purchasing in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
