working_alone_premise = 20
working_alone_hypothesis = 10

# the hypothesis talks about the time it takes Annie to do a job working alone, referenced also in the premise
if working_alone_hypothesis <= working_alone_premise:
    # check if the hypothesis value contradicts the estimate of less than 'working_alone_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the time it takes Annie to do the job working alone, but the hypothesis value is lower than that estimate
    # any time lower than 'working_alone_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
