# Premise: Max owns 200 shares of stock A and 180 of stock b.
# Hypothesis: Max owns less than 700 shares of stock A and 180 of stock b.
# Golden Label: entailment

stock_a_premise = 200
stock_a_hypothesis = 700
stock_b_premise = 180
stock_b_hypothesis = 180

# the hypothesis refers to the number of shares of stocks A and B mentioned in the premise
if stock_a_premise >= stock_a_hypothesis:
    # check if the estimate of 'stock_a_hypothesis' contradicts the number of shares of stock A in the premise
    label = "contradiction"
elif stock_b_hypothesis != stock_b_premise:
    # check if the number of shares of stock B in the hypothesis contradicts the number of shares of stock B reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

