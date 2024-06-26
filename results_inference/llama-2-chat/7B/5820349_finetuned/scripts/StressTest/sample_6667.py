work_completion_premise = 40
work_completion_hypothesis = 20

# the hypothesis refers to the time Kamal will take to complete work, which is also mentioned in the premise
if work_completion_hypothesis >= work_completion_premise:
    # check if the hypothesis value contradicts the estimate of less than 'work_completion_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time to complete work
    # any time less than 'work_completion_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
