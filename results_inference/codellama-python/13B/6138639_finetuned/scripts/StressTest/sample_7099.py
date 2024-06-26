marks_premise = 86
marks_hypothesis = 36

# the hypothesis talks about the marks of Reema, referenced also in the premise
if marks_hypothesis >= marks_premise:
    # check if the hypothesis value contradicts the estimate of less than'marks_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the marks
    # any marks less than'marks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
