# the hypothesis talks about the time when Jose joined him, referenced also in the premise
if hypothesis_time_joined_premise >= hypothesis_time_joined_hypothesis:
    # check if the time when Jose joined in the hypothesis contradicts the estimate of less than 'hypothesis_time_joined_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time when Jose joined
    # any time when Jose joined less than 'hypothesis_time_joined_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
