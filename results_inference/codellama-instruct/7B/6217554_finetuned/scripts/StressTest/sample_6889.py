seats_premise = 8
seats_hypothesis = 6

# the hypothesis talks about the number of people that can be seated on a bench, referenced also in the premise
if seats_hypothesis >= seats_premise:
    # check if the number of people in the hypothesis contradicts the estimate of less than'seats_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people
    # any number of people less than'seats_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
