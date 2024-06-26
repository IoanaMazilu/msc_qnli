girls_premise = 2
boys_premise = 2

# the hypothesis talks about the number of girls and boys mentioned in the premise
if girls_premise <= boys_premise:
    # check if the hypothesis value contradicts the estimate of more than 'girls_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of girls
    # any number of girls greater than 'girls_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
