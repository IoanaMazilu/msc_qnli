dan_job_premise = 85
dan_job_hypothesis = 15

# the hypothesis refers to the time it takes Dan to do a job alone
if dan_job_premise <= dan_job_hypothesis:
    # check if the hypothesis value contradicts the estimate of less than 'dan_job_premise'
    label = "contradiction"
elif dan_job_hypothesis!= dan_job_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value and the premise value are consistent, we can infer neutrality
    label = "neutral"

print(label)
