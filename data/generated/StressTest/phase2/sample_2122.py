# Premise: If the rosters for Professor Wang's more than 1 classes are combined with no student's name listed more than once, how many names will be on the combined roster?
# Hypothesis: If the rosters for Professor Wang's 3 classes are combined with no student's name listed more than once, how many names will be on the combined roster?
# Golden Label: neutral

classes_premise = 1
classes_hypothesis = 3

# the hypothesis talks about the number of Professor Wang's classes, referenced also in the premise
if classes_hypothesis <= classes_premise:
    # check if the hypothesis value contradicts the estimate of more than 'classes_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of classes
    # any number of classes greater than 'classes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

