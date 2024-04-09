birds_premise = 2
birds_hypothesis = 4
speed_premise = 7
speed_hypothesis = 1

# the hypothesis talks about the speed of the birds, which is also mentioned in the premise
if birds_hypothesis <= birds_premise:
    # check if the hypothesis value contradicts the estimate of less than 'birds_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of the birds
    # any speed greater than 'birds_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
