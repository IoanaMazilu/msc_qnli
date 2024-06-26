less_than_5000_premise = 5000
withdraws_rs_hypothesis = 2000

# the hypothesis talks about the amount of money Tony withdraws, referenced also in the premise
if less_than_5000_premise <= withdraws_rs_hypothesis:
    # check if the hypothesis value contradicts the estimate of less than 'less_than_5000_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money Tony withdraws
    # any amount of money withdrawn less than 'less_than_5000_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
