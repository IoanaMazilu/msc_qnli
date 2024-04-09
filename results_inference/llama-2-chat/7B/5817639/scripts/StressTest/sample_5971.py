run_time_premise = float(6)
run_time_hypothesis = float(7)

# the hypothesis talks about the time taken by Henry to run the second leg of the course
if run_time_hypothesis <= run_time_premise:
    # check if the hypothesis value contradicts the estimate of more than 'run_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time taken by Henry
    # any time taken by Henry that is greater than 'run_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
