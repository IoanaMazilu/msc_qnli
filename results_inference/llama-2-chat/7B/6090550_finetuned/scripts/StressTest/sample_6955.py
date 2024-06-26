average_shirts_premise = 80
average_shirts_hypothesis = 40
shirts_purchased_premise = 8
shirts_purchased_hypothesis = 8

# the hypothesis talks about the average number of shirts each person has after purchasing 8 shirts each
if average_shirts_hypothesis > average_shirts_premise:
    # check if the average number of shirts in the hypothesis contradicts the average number of shirts in the premise
    label = "contradiction"
elif average_shirts_hypothesis < average_shirts_premise:
    # check if the average number of shirts in the hypothesis is less than the average number of shirts in the premise
    label = "entailment"
else:
    # if the average number of shirts in the hypothesis does not contradict or entail the premise, it is neutral
    label = "neutral"

print(label)
