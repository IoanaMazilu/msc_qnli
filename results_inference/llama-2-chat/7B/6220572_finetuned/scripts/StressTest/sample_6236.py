doubled_speed_premise = 2
doubled_speed_hypothesis = 3

# the hypothesis talks about the time needed to clean the house if Anne's speed were doubled, referenced also in the premise
if doubled_speed_hypothesis <= doubled_speed_premise:
    # check if the hypothesis value contradicts the estimate of more than 'doubled_speed_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time needed to clean the house
    # any time less than 'doubled_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
