nifty_price_premise = 7500
nifty_price_hypothesis = 7400

# the hypothesis and premise mention the nifty price
if nifty_price_hypothesis > nifty_price_premise:
    # check if the nifty price in the hypothesis contradicts the nifty price in the premise
    label = "contradiction"
elif nifty_price_hypothesis < nifty_price_premise:
    # check if the nifty price in the hypothesis is less than the nifty price in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
#