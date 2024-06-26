people_bacci_premise = 63
people_bacci_hypothesis = 13

# the hypothesis talks about the number of people in a BCCI meeting, referenced also in the premise
if people_bacci_hypothesis >= people_bacci_premise:
    # check if the hypothesis value contradicts the estimate of less than 'people_bacci_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people
    # any number of people less than 'people_bacci_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
