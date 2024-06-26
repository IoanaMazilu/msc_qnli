work_start_time_premise = 1
work_start_time_hypothesis = 8

# The hypothesis talks about the beginning work time of Vikas, referenced also in the premise
if work_start_time_hypothesis <= work_start_time_premise:
    # Check if the hypothesis value contradicts the estimate of Vikas beginning work at more than 'work_start_time_premise'
    label = "contradiction"
else:
    # The premise gives only an estimate for the beginning work time
    # Any beginning time greater than 'work_start_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
