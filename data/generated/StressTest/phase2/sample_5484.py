# Premise: Patrick has a locker with a 3 number combination.
# Hypothesis: Patrick has a locker with a less than 8 number combination.
# Golden Label: entailment

locker_combination_premise = 3
locker_combination_hypothesis = 8

# the hypothesis is referring to the number of the locker combination mentioned in the premise
if locker_combination_premise >= locker_combination_hypothesis:
    # check if the number of locker combination in the premise contradicts the hypothesis estimate of less than 'locker_combination_hypothesis'
    label = "contradiction"
elif locker_combination_premise < locker_combination_hypothesis:
    # check if the number of locker combination in the premise can be fully entailed by the hypothesis
    label = "entailment"
else:
    # if the hypothesis value does not contradict the premise one, but also cannot be fully and explicitly entailed from the premise
    label = "neutral"

print(label)

