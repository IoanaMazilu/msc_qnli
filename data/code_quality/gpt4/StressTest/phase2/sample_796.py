shirts_premise = 60
shirts_hypothesis = 10
pants_premise = 8
pants_hypothesis = 8

# the hypothesis refers to the number of shirts and pants Barbara has, mentioned in the premise
if shirts_hypothesis >= shirts_premise:
    # check if the number of shirts in the hypothesis contradicts the estimate of less than 'shirts_premise'
    label = "contradiction"
elif pants_hypothesis != pants_premise:
    # check if the number of pants in the hypothesis contradicts the number of pants in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
