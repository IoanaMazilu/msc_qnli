# Premise: Johnny has 4 classes.
# Hypothesis: Johnny has 2 classes.
# Golden Label: contradiction

classes_premise = 4
classes_hypothesis = 2

# the hypothesis talks about the number of classes Johnny has, also referenced in the premise
if classes_premise != classes_hypothesis:
    # check if the number of classes in the hypothesis contradicts the number of classes reported in the premise
    label = "contradiction"
else:
    # if the number of classes in the hypothesis does not contradict the premise, then entailment can be inferred
    label = "entailment"

print(label)

