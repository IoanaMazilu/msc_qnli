marks_premise = [56, 60, 72, 85, 80]
marks_hypothesis = [26, 60, 72, 85, 80]

# the hypothesis refers to the marks obtained in different subjects as mentioned in the premise
if any(marks_hypothesis[i] <= marks_premise[i] for i in range(len(marks_hypothesis))):
    # check if any of the marks in the hypothesis contradicts the marks reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average marks
    # any average marks greater than'marks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
