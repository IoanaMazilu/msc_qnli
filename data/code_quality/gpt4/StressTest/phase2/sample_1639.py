joining_time_premise = 6
joining_time_hypothesis = 2

# the hypothesis talks about the time Sujeet joined, referenced also in the premise
if joining_time_hypothesis > joining_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'joining_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time Sujeet joined
    # any time less than 'joining_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
