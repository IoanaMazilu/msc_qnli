opec_cuts_premise = 28
opec_cuts_hypothesis = 68

# the hypothesis talks about the percentage of price decrease in crude oil in the last 3 months
if opec_cuts_hypothesis <= opec_cuts_premise:
    # check if the hypothesis value contradicts the estimate of less than 'opec_cuts_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the percentage of price decrease in crude oil
    # any percentage of price decrease less than 'opec_cuts_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
