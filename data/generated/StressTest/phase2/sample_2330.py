# Premise: If the rosters for Professor Wang's 3 classes are combined with no student's name listed more than once, how many names will be on the combined roster?
# Hypothesis: If the rosters for Professor Wang's less than 3 classes are combined with no student's name listed more than once, how many names will be on the combined roster?
# Golden Label: contradiction

classes_premise = 3
classes_hypothesis = 3

# the hypothesis refers to the number of classes mentioned in the premise
if classes_premise != classes_hypothesis:
    # check if the number of classes in the hypothesis contradicts the number of classes in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

