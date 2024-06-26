sensex_premise = 103
sensex_hypothesis = 100
nifty_premise = 8900
nifty_hypothesis = 8900

# the hypothesis and premise mention the same values for the Sensex and Nifty indices
if sensex_hypothesis!= sensex_premise:
    # check if the Sensex value in the hypothesis contradicts the premise value
    label = "contradiction"
elif nifty_hypothesis!= nifty_premise:
    # check if the Nifty value in the hypothesis contradicts the premise value
    label = "contradiction"
else:
    # the premise gives only an estimate for the values of the indices
    # any estimate of the values in the hypothesis greater or equal to the premise values is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
