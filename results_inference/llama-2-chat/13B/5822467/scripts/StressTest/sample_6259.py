dan_job_premise = 25
dan_job_hypothesis = 15

# the hypothesis refers to the time required to complete a job alone
if dan_job_premise <= dan_job_hypothesis:
    # check if the hypothesis value contradicts the estimate of less than 'dan_job_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time required
    # any time less than or equal to 'dan_job_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
