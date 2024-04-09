opec_cuts_premise = 68
opec_cuts_hypothesis = 28

# the hypothesis talks about the percentage change in crude oil price after OPEC cuts, referenced also in the premise
if opec_cuts_hypothesis <= opec_cuts_premise:
    # check if the hypothesis value contradicts the estimate of less than 'opec_cuts_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage change in crude oil price
    # any percentage change greater than 'opec_cuts_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
