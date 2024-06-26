join_time_premise = 8
join_time_hypothesis = 2

# the hypothesis talks about the time when Jose joined, referenced also in the premise
if join_time_hypothesis >= join_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'join_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time when Jose joined
    # any time less than 'join_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
