marks_premise = [66, 65, 82, 67, 85]
marks_hypothesis = [76, 65, 82, 67, 85]

# the hypothesis talks about the marks obtained by Arun in the subjects, as mentioned in the premise
for subject in marks_premise:
    if marks_hypothesis[subject] <= marks_premise[subject]:
        # check if the hypothesis value contradicts the estimate of'marks_premise[subject]'
        label = "contradiction"
        break
else:
    # the premise gives only an estimate for the marks obtained by Arun in each subject
    # any marks greater than'marks_premise[subject]' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
