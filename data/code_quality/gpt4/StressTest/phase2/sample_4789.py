people_meeting_premise = 31
people_meeting_hypothesis = 11

# the hypothesis talks about the number of people in the BCCI meeting, referenced also in the premise
if people_meeting_hypothesis >= people_meeting_premise:
    # check if the hypothesis value contradicts the estimate of less than 'people_meeting_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people
    # any number of people less than 'people_meeting_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
