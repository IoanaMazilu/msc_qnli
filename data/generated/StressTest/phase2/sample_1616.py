# Premise: If the rosters for Professor Wang's 3 classes are combined with no student's name listed more than once, how many names will be on the combined roster?
# Hypothesis: If the rosters for Professor Wang's 8 classes are combined with no student's name listed more than once, how many names will be on the combined roster?
# Golden Label: contradiction

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

