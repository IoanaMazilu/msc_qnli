# define the variables
classes_premise = 3
classes_hypothesis = 8

# the hypothesis refers to the number of classes of Professor Wang in the premise
if classes_premise != classes_hypothesis:
    # check if the number of classes in the hypothesis contradicts the number of classes in the premise
    label = "contradiction"
else:
    # the hypothesis and the premise are the same
    label = "entailment"

print(label)
