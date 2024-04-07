# Premise: An investor can sell her MicroTron stock for less than 76 $per share and her Dynaco stock for 48 $per share, If she sells 300 shares altogether, some of each stock, at an average price per share of 40 $, how many shares of Dynaco stock has she sold?
# Hypothesis: An investor can sell her MicroTron stock for 36 $per share and her Dynaco stock for 48 $per share, If she sells 300 shares altogether, some of each stock, at an average price per share of 40 $, how many shares of Dynaco stock has she sold?
# Golden Label: neutral

microtron_stock_price_premise = 76
microtron_stock_price_hypothesis = 36
dynaco_stock_price_premise = 48
dynaco_stock_price_hypothesis = 48
total_shares_premise = 300
total_shares_hypothesis = 300
average_price_premise = 40
average_price_hypothesis = 40

# the hypothesis refers to the same situation as the premise, with a different price per share for MicroTron stock
if microtron_stock_price_hypothesis >= microtron_stock_price_premise:
    # check if the price per share for MicroTron stock in the hypothesis contradicts the estimate of less than 'microtron_stock_price_premise' in the premise
    label = "contradiction"
elif dynaco_stock_price_hypothesis != dynaco_stock_price_premise or total_shares_hypothesis != total_shares_premise or average_price_hypothesis != average_price_premise:
    # check if the price per share for Dynaco stock, total shares, or average price per share in the hypothesis contradicts the values in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

