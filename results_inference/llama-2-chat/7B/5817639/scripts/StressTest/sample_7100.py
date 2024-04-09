marks_premise = 66
marks_hypothesis = 36

# the hypothesis talks about the marks secured by Reema, referenced also in the premise
if marks_hypothesis <= marks_premise:
    # check if the hypothesis value contradicts the estimate of'marks_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of roses
    # any number of roses greater than 'roses_vase_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
