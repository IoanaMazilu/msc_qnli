# Premise: Johnny has more than 1 classes.
# Hypothesis: Johnny has 4 classes.
# Golden Label: neutral

classes_premise = 1
classes_hypothesis = 4

# the hypothesis states a specific number of classes Johnny has, which is also referenced in the premise
if classes_hypothesis <= classes_premise:
    # check if the hypothesis value contradicts the premise estimate of more than 'classes_premise'
    label = "contradiction"
else:
    # the premise provides only an estimate for the number of classes
    # any number of classes greater than 'classes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

