sensex_premise = 103
sensex_hypothesis = 100
nifty_premise = 8900
nifty_hypothesis = 8900
stock_option_premise = 0
stock_option_hypothesis = 0

# the hypothesis mentions the rise in Sensex and Nifty, but not the Stock Option calls
if sensex_hypothesis!= sensex_premise:
    # check if the rise in Sensex in the hypothesis contradicts the rise in Sensex in the premise
    label = "contradiction"
elif nifty_hypothesis!= nifty_premise:
    # check if the rise in Nifty in the hypothesis contradicts the rise in Nifty in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
