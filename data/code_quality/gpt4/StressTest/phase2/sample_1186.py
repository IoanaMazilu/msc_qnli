girls_premise = 2
girls_hypothesis = 4

# the hypothesis talks about the number of girls dating boys, referenced also in the premise
if girls_hypothesis <= girls_premise:
    # check if the hypothesis number of girls contradicts the estimate of more than 'girls_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of girls
    # any number of girls greater than 'girls_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
