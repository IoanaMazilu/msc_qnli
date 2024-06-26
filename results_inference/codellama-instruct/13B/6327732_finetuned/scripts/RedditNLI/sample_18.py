premise_sensex_close = 362.75
hypothesis_sensex_down = 357.39

# the hypothesis mentions the Sensex closing lower than the premise
if hypothesis_sensex_down < premise_sensex_close:
    label = "entailment"
else:
    label = "neutral"

print(label)
