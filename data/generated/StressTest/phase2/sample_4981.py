# Premise: If the rosters for Professor Wang's less than 6 classes are combined with no student's name listed more than once, how many names will be on the combined roster?
# Hypothesis: If the rosters for Professor Wang's 3 classes are combined with no student's name listed more than once, how many names will be on the combined roster?
# Golden Label: neutral

classes_premise = 6
classes_hypothesis = 3

# the hypothesis refers to the number of Professor Wang's classes mentioned in the premise
if classes_hypothesis >= classes_premise:
    # check if the number of classes in the hypothesis contradicts the number of classes in the premise
    label = "contradiction"
else:
    # the premise gives an upper limit for the number of classes
    # any number of classes less than 'classes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

