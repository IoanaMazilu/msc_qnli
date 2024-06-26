classes_premise = 3
classes_hypothesis = 2

# the hypothesis refers to the number of Professor Wang's classes mentioned in the premise
if classes_premise <= classes_hypothesis:
    # check if the hypothesis value contradicts the number of classes in the premise
    label = "contradiction"
elif classes_premise > classes_hypothesis:
    # the premise gives an exact number of classes, the hypothesis gives an estimate for the number of classes
    # any number of classes greater than 'classes_hypothesis' is consistent with the hypothesis, but cannot be explicitly entailed from the hypothesis
    label = "entailment"

print(label)
