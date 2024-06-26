work_start_time_premise = 8
work_start_time_hypothesis = 1

# the hypothesis talks about the start time of Vikas's work shift, referenced also in the premise
if work_start_time_hypothesis >= work_start_time_premise:
    # check if the hypothesis value contradicts the premise, which states that Vikas starts at 8 a.m.
    label = "contradiction"
else:
    # the premise gives a specific start time for Vikas's work shift
    # any start time earlier than 'work_start_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
