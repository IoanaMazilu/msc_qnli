marks_premise = [86, 75, 52, 68, 89]
marks_hypothesis = [66, 75, 52, 68, 89]

# the hypothesis talks about the marks obtained by Nancy in different subjects, referenced also in the premise
for mark in marks_hypothesis:
    if mark >= marks_premise[0]:
        # check if the hypothesis mark contradicts the premise's estimate of less than'marks_premise[0]'
        label = "contradiction"
        break
else:
    # the premise gives only an estimate for the marks
    # any marks less than'marks_premise[0]' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
