chiefs_meeting_premise = 6
chiefs_meeting_hypothesis = 7

# the hypothesis talks about the number of Joint Chiefs of Staff at a meeting, referenced also in the premise
if chiefs_meeting_hypothesis <= chiefs_meeting_premise:
    # check if the hypothesis value contradicts the estimate of more than 'chiefs_meeting_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of Joint Chiefs of Staff
    # any number of chiefs greater than 'chiefs_meeting_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
