nifty_price_premise = 7500
nifty_price_hypothesis = 7400

# the hypothesis talks about the price of nifty, which is also mentioned in the premise
if nifty_price_hypothesis <= nifty_price_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is greater than the premise value, it is entailed
    label = "entailment"

print(label)
