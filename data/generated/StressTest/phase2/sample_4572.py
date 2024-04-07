# Premise: Susan, John, Daisy, Tim and Kim need to be seated in 5 identical chairs in straight line so that Susan is seated always left to Tim.
# Hypothesis: Susan, John, Daisy, Tim and Kim need to be seated in more than 4 identical chairs in straight line so that Susan is seated always left to Tim.
# Golden Label: entailment

chairs_premise = 5
chairs_hypothesis = 4

# The hypothesis refers to the number of chairs mentioned in the premise
if chairs_premise <= chairs_hypothesis:
    # Check if 'chairs_hypothesis' contradicts the number of chairs in the premise
    label = "contradiction"
else:
    # If the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

