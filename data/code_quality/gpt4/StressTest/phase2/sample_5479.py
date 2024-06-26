people_premise = 5
people_hypothesis = 3

# the hypothesis talks about the number of people who voted to watch a certain show, mentioned also in the premise
if people_hypothesis >= people_premise:
    # check if the number of people in the hypothesis contradicts the estimate of less than 'people_premise' in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people
    # any number of people less than 'people_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
