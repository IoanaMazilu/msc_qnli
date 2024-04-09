marks_premise = float(56)
marks_hypothesis = float(46)

# the hypothesis talks about the marks secured by Reema, referenced also in the premise
if marks_hypothesis <= marks_premise:
    # check if the hypothesis value contradicts the estimate of'marks_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the marks, and any marks value greater than'marks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
