# Premise: Nifty50 at 8,400, Sensex ends in Red, Investment Advisory Company In Indore.
# Hypothesis: Nifty below 8400, Sensex In RED, Stock Advisory Company In Indore.
# Golden Label: contradiction

nifty_premise = 8400
nifty_hypothesis = 8400

# the hypothesis and premise mention nifty value
if nifty_hypothesis >= nifty_premise:
    # check if the nifty value in the hypothesis contradicts the premise of being at 'nifty_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

