# Premise: Gold tops $1500/oz for he first time.
# Hypothesis: Gold Reaches $1500 For First Time In History.
# Golden Label: contradiction

gold_price_premise = 1500
gold_price_hypothesis = 1500

# the hypothesis and premise both mention the price of gold topping a particular value
if gold_price_premise != gold_price_hypothesis:
    # check if the price of gold in the hypothesis contradicts the price of gold in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

