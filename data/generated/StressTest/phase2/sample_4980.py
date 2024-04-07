# Premise: If the rosters for Professor Wang's 3 classes are combined with no student's name listed more than once, how many names will be on the combined roster?
# Hypothesis: If the rosters for Professor Wang's less than 6 classes are combined with no student's name listed more than once, how many names will be on the combined roster?
# Golden Label: entailment

classes_premise = 3
classes_hypothesis = 6

# The hypothesis refers to the number of Professor Wang's classes mentioned in the premise
if classes_hypothesis < classes_premise:
    # check if the 'classes_hypothesis' contradicts the number of classes in the premise
    label = "contradiction"
elif classes_hypothesis > classes_premise:
    # check if the 'classes_hypothesis' contradicts the number of classes in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

