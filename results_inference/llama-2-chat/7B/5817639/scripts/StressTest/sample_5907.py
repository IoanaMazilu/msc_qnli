marks_premise = [76, 65, 82, 67, 75]
marks_hypothesis = [46, 65, 82, 67, 75]

# the hypothesis talks about the marks scored by Shekar in different subjects, referenced also in the premise
for subject in marks_premise:
    if marks_hypothesis[subject] <= marks_premise[subject]:
        # check if the hypothesis value contradicts the estimate of marks scored by Shekar in the premise
        label = "contradiction"
    else:
        # the premise gives only an estimate for the marks scored by Shekar in each subject
        # any marks scored by Shekar greater than the estimate in the premise is consistent with the premise, but cannot be explicitly entailed from the premise
        label = "neutral"
print(label)
