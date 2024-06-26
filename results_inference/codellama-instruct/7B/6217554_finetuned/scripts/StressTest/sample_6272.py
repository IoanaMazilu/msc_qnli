participants_race_premise = 7
participants_race_hypothesis = 2

if participants_race_hypothesis >= participants_race_premise:
    # check if the hypothesis value contradicts the estimate of more than 'participants_race_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of participants
    # any number of participants greater than 'participants_race_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
