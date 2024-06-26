marks_premise = 50
marks_hypothesis = 60

# the hypothesis refers to the marks of Reema mentioned in the premise
if marks_hypothesis <= marks_premise:
    # check if the estimate of'marks_hypothesis' contradicts the number of marks in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the marks
    # any number of marks less than'marks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
