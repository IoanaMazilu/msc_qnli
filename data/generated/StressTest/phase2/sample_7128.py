# Premise: Anup was asked to find the value of 7/12 of a sum of money T.
# Hypothesis: Anup was asked to find the value of more than 4/12 of a sum of money T.
# Golden Label: entailment

value_premise = 7/12
value_hypothesis = 4/12

# the hypothesis refers to the value Anup was asked to find, mentioned in the premise
if value_premise <= value_hypothesis:
    # check if the value 'value_hypothesis' contradicts the value in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

