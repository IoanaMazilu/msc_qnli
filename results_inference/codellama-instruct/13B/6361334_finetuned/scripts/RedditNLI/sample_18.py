premise_sensex_close = 362.75
hypothesis_sensex_down = 357.39

# the hypothesis and premise mention the closing price of the Sensex and the Nifty
if premise_sensex_close!= hypothesis_sensex_down:
    # check if the closing price in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the closing price in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
