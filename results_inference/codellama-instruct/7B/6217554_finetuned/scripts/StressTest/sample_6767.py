people_bcc_meeting_premise = 13
people_bcc_meeting_hypothesis = 13

if people_bcc_meeting_hypothesis >= people_bcc_meeting_premise:
    # check if the hypothesis value contradicts the number of people in the premise
    label = "contradiction"
else:
    # the hypothesis gives an estimate for the number of people in the meeting
    # any number of people less than 'people_bcc_meeting_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "entailment"

print(label)
