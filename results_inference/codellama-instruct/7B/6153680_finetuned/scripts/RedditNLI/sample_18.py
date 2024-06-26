sensex_premise = 362.75
sensex_hypothesis = 357.39
nifty_hypothesis = "Nifty future tips"

# the hypothesis mentions the SENSEX and Nifty indices being down, which is also mentioned in the premise
if sensex_hypothesis < sensex_premise:
    label = "contradiction"
elif nifty_hypothesis == "Nifty future tips":
    label = "neutral"
else:
    label = "entailment"

print(label)
