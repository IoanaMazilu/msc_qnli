horses_premise = 4
horses_hypothesis = 3
total_horses_premise = 25
total_horses_hypothesis = 25

# the hypothesis talks about the number of horses the London Racetrack needs to submit to the Kentucky Derby, referenced also in the premise
if horses_hypothesis >= horses_premise:
    # check if the hypothesis value contradicts the estimate of less than 'horses_premise'
    label = "contradiction"
elif total_horses_hypothesis!= total_horses_premise:
    # check if the total number of horses in the hypothesis contradicts the total number of horses reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of horses
    # any number of horses less than 'horses_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
