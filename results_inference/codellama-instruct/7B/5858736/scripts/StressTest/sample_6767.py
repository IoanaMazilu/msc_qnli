people_bcc_premise = 13
people_bcc_hypothesis = 13

# the hypothesis talks about the number of people in a BCCI meeting, referenced also in the premise
if people_bcc_hypothesis >= people_bcc_premise:
    # check if the hypothesis value contradicts the estimate of less than 'people_bcc_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people
    # any number of people less than 'people_bcc_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
