stock_a_premise = 200
stock_a_hypothesis = 200
stock_b_premise = 180
stock_b_hypothesis = 180

# the hypothesis refers to the number of shares of stock A and B owned by Max, as mentioned in the premise
if stock_a_hypothesis > stock_a_premise:
    # check if the hypothesis value contradicts the number of shares of stock A owned by Max in the premise
    label = "contradiction"
elif stock_b_hypothesis != stock_b_premise:
    # check if the number of shares of stock B owned by Max in the hypothesis contradicts the number of shares of stock B owned by Max in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
