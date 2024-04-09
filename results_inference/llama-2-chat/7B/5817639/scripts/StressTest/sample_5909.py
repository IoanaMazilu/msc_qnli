marks_premise = [76, 65, 82, 67, 75]
marks_hypothesis = [87, 85, 90, 88, 95]

# the hypothesis talks about the marks scored by Shekar in different subjects
for subject in marks_premise:
    if marks_hypothesis[subject] <= marks_premise[subject]:
        # check if the hypothesis value contradicts the estimate of marks scored in the premise
        label = "contradiction"
    else:
        # the premise gives only an estimate for the marks scored in each subject
        # any marks score greater than the premise estimate is consistent with the premise, but cannot be explicitly entailed from the premise
        label = "neutral"
print(label)
