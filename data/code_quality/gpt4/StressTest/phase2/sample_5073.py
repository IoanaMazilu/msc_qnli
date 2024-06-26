avg_shirts_premise = 60
avg_shirts_hypothesis = 10
shirts_purchased_each = 5

# the hypothesis refers to the average number of shirts with Salman, Ambani and Dalmiya mentioned in the premise
if avg_shirts_premise <= avg_shirts_hypothesis:
    # check if the estimate of 'avg_shirts_hypothesis' contradicts the average number of shirts in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
