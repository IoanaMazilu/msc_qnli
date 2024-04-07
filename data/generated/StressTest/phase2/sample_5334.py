# Premise: Anup was asked to find the value of 7/12 of a sum of money W.
# Hypothesis: Anup was asked to find the value of more than 5/12 of a sum of money W.
# Golden Label: entailment

portion_premise = 7/12
portion_hypothesis = 5/12

# the hypothesis refers to the portion of money Anup was asked to find in the premise
if portion_premise <= portion_hypothesis:
    # check if the portion in the hypothesis contradicts the portion in the premise
    label = "contradiction"
elif portion_premise > portion_hypothesis:
    # check if the portion in the premise entails the hypothesis
    label = "entailment"
else:
    # if the hypothesis value does not contradict or is not entailed by the premise, we infer neutrality
    label = "neutral"

print(label)

