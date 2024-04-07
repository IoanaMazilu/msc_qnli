# Premise: If the rosters for Professor Wang's less than 5 classes are combined with no student's name listed more than once, how many names will be on the combined roster?
# Hypothesis: If the rosters for Professor Wang's 3 classes are combined with no student's name listed more than once, how many names will be on the combined roster?
# Golden Label: neutral

classes_premise = 5
classes_hypothesis = 3

# the hypothesis refers to the number of Professor Wang's classes mentioned in the premise
if classes_hypothesis >= classes_premise:
    # check if the number of 'classes_hypothesis' contradicts the number of classes in the premise
    label = "contradiction"
elif classes_hypothesis < classes_premise:
    # if the number of classes in the hypothesis is less than the number of classes in the premise
    # the hypothesis does not contradict the premise, but cannot be fully and explicitly entailed from the premise
    label = "neutral"

print(label)

