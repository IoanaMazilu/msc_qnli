marks_premise = [26, 60, 72, 85, 80]
marks_hypothesis = [56, 60, 72, 85, 80]

# the hypothesis refers to the marks obtained by a student in the same subjects as the premise
if marks_hypothesis!= marks_premise:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
else:
    # the premise gives only an estimate for the marks obtained by a student
    # any number of marks greater than'marks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
