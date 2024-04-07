# Premise: An investor can sell her MicroTron stock for 36 $per share and her Dynaco stock for 68 $per share, If she sells 300 shares altogether, some of each stock, at an average price per share of 40 $, how many shares of Dynaco stock has she sold?
# Hypothesis: An investor can sell her MicroTron stock for less than 36 $per share and her Dynaco stock for 68 $per share, If she sells 300 shares altogether, some of each stock, at an average price per share of 40 $, how many shares of Dynaco stock has she sold?
# Golden Label: contradiction

microtron_share_price_premise = 36
microtron_share_price_hypothesis = 36
dynaco_share_price_premise = 68
dynaco_share_price_hypothesis = 68
total_shares_premise = 300
total_shares_hypothesis = 300
average_price_premise = 40
average_price_hypothesis = 40

# The hypothesis refers to the prices of MicroTron and Dynaco stocks, the total number of shares, and the average price per share mentioned in the premise
if microtron_share_price_hypothesis >= microtron_share_price_premise:
    # Check if the estimate of 'microtron_share_price_hypothesis' contradicts the price of MicroTron shares in the premise
    label = "contradiction"
elif total_shares_hypothesis != total_shares_premise or average_price_hypothesis != average_price_premise or dynaco_share_price_hypothesis != dynaco_share_price_premise:
    # Check if the number of total shares, the average price per share, or the price of Dynaco shares in the hypothesis contradicts the respective values reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

