rosy_premise = 10
mary_premise = 10

# the hypothesis talks about the efficiency of Rosy and Mary, referenced also in the premise
if rosy_premise <= mary_premise:
    # check if the hypothesis value contradicts the estimate of 'rosy_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the efficiency of Rosy
    # any number of efficiency greater than 'rosy_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
