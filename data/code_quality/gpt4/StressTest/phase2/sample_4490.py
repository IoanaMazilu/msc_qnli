work_time_premise = 20
work_time_hypothesis = 20

# the hypothesis talks about the time Sakshi can do a piece of work, which is also mentioned in the premise
if work_time_hypothesis >= work_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'work_time_premise'
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise, it can't be explicitly entailed from the premise
    label = "neutral"

print(label)
