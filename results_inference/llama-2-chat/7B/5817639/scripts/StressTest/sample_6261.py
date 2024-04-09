working_alone_premise = 10
working_alone_hypothesis = 40

# the hypothesis talks about the time it takes Annie to complete the job, referenced also in the premise
if working_alone_hypothesis >= working_alone_premise:
    # check if the hypothesis value contradicts the estimate of 'working_alone_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the time it takes Annie to complete the job, while the hypothesis provides a larger estimate
    # any time greater than 'working_alone_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
