job_alone_premise = 85
job_alone_hypothesis = 15

# the hypothesis talks about the time it takes Dan to do a job alone, referenced also in the premise
if job_alone_hypothesis <= job_alone_premise:
    # check if the hypothesis value contradicts the estimate of less than 'job_alone_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the time it takes Dan to do a job alone, which is consistent with the hypothesis
    label = "entailment"

print(label)
