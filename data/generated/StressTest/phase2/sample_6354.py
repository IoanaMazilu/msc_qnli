# Premise: An investor can sell her MicroTron stock for 36 $per share and her Dynaco stock for 48 $per share, If she sells 300 shares altogether, some of each stock, at an average price per share of 40 $, how many shares of Dynaco stock has she sold?
# Hypothesis: An investor can sell her MicroTron stock for less than 76 $per share and her Dynaco stock for 48 $per share, If she sells 300 shares altogether, some of each stock, at an average price per share of 40 $, how many shares of Dynaco stock has she sold?
# Golden Label: entailment

microtron_stock_price_premise = 36
microtron_stock_price_hypothesis = 76
dynaco_stock_price_premise = 48
dynaco_stock_price_hypothesis = 48
total_shares_premise = 300
total_shares_hypothesis = 300
average_price_premise = 40
average_price_hypothesis = 40

# the hypothesis refers to the prices of MicroTron and Dynaco stocks, total shares sold and average price per share mentioned in the premise
if microtron_stock_price_hypothesis < microtron_stock_price_premise or dynaco_stock_price_hypothesis != dynaco_stock_price_premise:
    # check if the prices of MicroTron or Dynaco stocks in the hypothesis contradict the prices in the premise
    label = "contradiction"
elif total_shares_hypothesis != total_shares_premise or average_price_hypothesis != average_price_premise:
    # check if the total shares sold or the average price per share in the hypothesis contradict the values in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

