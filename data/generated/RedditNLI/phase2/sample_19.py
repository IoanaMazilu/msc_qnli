# Premise: Sensex high 20000 touch, Nifty above 5900, Tuesday stock market positive and sure nifty future trading call on today.
# Hypothesis: SENSEX & Nifty down, Sensex down 357.39 Pts, Nifty future tips, Intraday stock future trading call tomorrow, today nifty future call.
# Golden Label: contradiction

sensex_premise = 20000
nifty_premise = 5900
sensex_hypothesis = -357.39

# the hypothesis and premise mention the performance of Sensex and Nifty
if sensex_hypothesis > sensex_premise:
    # check if the Sensex performance in the hypothesis contradicts the Sensex performance in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the performance of the Sensex and Nifty
    # any estimate of the performance in the hypothesis lower than or equal to 'sensex_premise' and 'nifty_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

