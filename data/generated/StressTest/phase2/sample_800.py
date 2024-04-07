# Premise: How many clothing combinations does Barbara have, if she doesn’t wear 2 specific shirts with 3 specific pants?
# Hypothesis: How many clothing combinations does Barbara have, if she doesn’t wear less than 2 specific shirts with 3 specific pants?
# Golden Label: contradiction

shirts_premise = 2
shirts_hypothesis = 2
pants_premise = 3
pants_hypothesis = 3

# the hypothesis refers to the number of specific shirts and pants mentioned in the premise
if shirts_premise < shirts_hypothesis:
    # check if the number of 'shirts_hypothesis' contradicts the number of specific shirts in the premise
    label = "contradiction"
elif pants_hypothesis != pants_premise:
    # check if the number of specific pants in the hypothesis contradicts the number of specific pants in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

