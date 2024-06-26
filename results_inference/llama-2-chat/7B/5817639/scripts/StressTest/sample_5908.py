marks_premise = [46, 65, 82, 67, 75]
marks_hypothesis = [76, 65, 82, 67, 75]

# the hypothesis refers to the marks scored by Shekar in the subjects mentioned in the premise
if any(marks_hypothesis <= marks_premise):
    # check if the estimate of'marks_hypothesis' contradicts the marks scored in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the marks scored by Shekar in each subject
    # any marks scored greater than the premise values is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
