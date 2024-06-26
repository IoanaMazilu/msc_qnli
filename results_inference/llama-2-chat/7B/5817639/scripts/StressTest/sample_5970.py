run_time_premise = 7
run_time_hypothesis = 6

# the hypothesis talks about a faster run time than the premise
if run_time_hypothesis > run_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'run_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the run time
    # any run time faster than 'run_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
