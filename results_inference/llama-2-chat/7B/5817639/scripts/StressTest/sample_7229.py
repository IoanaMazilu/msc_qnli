marks_premise = [66, 75, 52, 68, 89]
marks_hypothesis = [86, 75, 52, 68, 89]

# the hypothesis talks about the marks obtained by Nancy in 5 subjects, mentioned in the premise
if marks_hypothesis <= marks_premise:
    # check if the hypothesis value contradicts the estimate of the marks obtained by Nancy in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the marks obtained by Nancy in each subject
    # any marks greater than the premise estimate is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
