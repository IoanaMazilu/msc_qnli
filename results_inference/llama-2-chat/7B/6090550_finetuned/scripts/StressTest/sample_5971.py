yapilabels_premise = 6
yapilabels_hypothesis = 7

# the hypothesis talks about the time Henry took to run the second leg of the course, referenced also in the premise
if yapilabels_hypothesis <= yapilabels_premise:
    # check if the hypothesis value contradicts the estimate of more than 'yapilabels_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time
    # any time greater than 'yapilabels_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

