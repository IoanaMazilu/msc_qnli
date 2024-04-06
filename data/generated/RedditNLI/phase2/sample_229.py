# Premise: Gold Reaches $1500 For First Time In History.
# Hypothesis: Gold tops $1500/oz for he first time.
# Golden Label: contradiction

gold_price_premise = 1500
gold_price_hypothesis = 1500

# the hypothesis and premise mention the price of gold
if gold_price_premise != gold_price_hypothesis:
    # check if the gold price in the hypothesis contradicts the gold price in the premise
    label = "contradiction"
else:
    # if the gold price in the hypothesis and premise are equal, we can infer entailment
    label = "entailment"

print(label)

