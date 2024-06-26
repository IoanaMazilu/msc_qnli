sensex_rise_premise = 103
sensex_rise_hypothesis = 100
nifty_end_premise = 8900
nifty_end_hypothesis = 8900

# both hypothesis and premise mention points rise in Sensex and Nifty's end value
if sensex_rise_hypothesis > sensex_rise_premise:
    # check if the Sensex rise points in the hypothesis contradicts the Sensex rise points in the premise
    label = "contradiction"
elif nifty_end_hypothesis != nifty_end_premise:
    # check if the Nifty end value in the hypothesis contradicts the Nifty end value in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
