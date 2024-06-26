marks_premise = [86, 75, 52, 68, 89]
marks_hypothesis = [66, 75, 52, 68, 89]

# the hypothesis talks about the marks obtained by Nancy in different subjects, referenced also in the premise
if any(mark_hypothesis >= mark_premise for mark_hypothesis, mark_premise in zip(marks_hypothesis, marks_premise)):
    # check if any of the marks in the hypothesis contradicts the estimate of less than'mark_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the marks
    # any marks less than'mark_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
