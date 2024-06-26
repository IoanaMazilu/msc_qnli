cigarettes_case_premise = 8
cigarettes_case_hypothesis = 5

# the hypothesis talks about the number of boxes of cigarettes in one case, referenced also in the premise
if cigarettes_case_hypothesis >= cigarettes_case_premise:
    # check if the hypothesis value contradicts the estimate of less than 'cigarettes_case_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of boxes of cigarettes
    # any number of boxes less than 'cigarettes_case_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
