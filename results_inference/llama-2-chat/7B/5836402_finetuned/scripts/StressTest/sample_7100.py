initial_marks_premise = 66
initial_marks_hypothesis = 36

# the hypothesis refers to the initial marks of Reema mentioned in the premise
if initial_marks_hypothesis <= initial_marks_premise:
    # check if the hypothesis value contradicts the estimate of more than 'initial_marks_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the initial marks
    # any initial marks greater than 'initial_marks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
