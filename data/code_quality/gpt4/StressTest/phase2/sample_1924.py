stock_a_premise = 700
stock_a_hypothesis = 200
stock_b_premise = 180
stock_b_hypothesis = 180

# the hypothesis refers to the number of shares Max owns of each stock, which is also mentioned in the premise
if stock_a_hypothesis >= stock_a_premise:
    # check if the number of shares of stock A in the hypothesis contradicts the estimate of less than 'stock_a_premise' shares in the premise
    label = "contradiction"
elif stock_b_hypothesis != stock_b_premise:
    # check if the number of shares of stock B in the hypothesis contradicts the number of shares reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of stock A shares
    # any number of shares less than 'stock_a_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
