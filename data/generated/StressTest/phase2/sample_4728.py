# Premise: An investor can sell her MicroTron stock for 36 $per share and her Dynaco stock for 56 $per share, If she sells 300 shares altogether, some of each stock, at an average price per share of 40 $, how many shares of Dynaco stock has she sold?
# Hypothesis: An investor can sell her MicroTron stock for more than 26 $per share and her Dynaco stock for 56 $per share, If she sells 300 shares altogether, some of each stock, at an average price per share of 40 $, how many shares of Dynaco stock has she sold?
# Golden Label: entailment

microtron_stock_price_premise = 36
microtron_stock_price_hypothesis = 26
dynaco_stock_price_premise = 56
dynaco_stock_price_hypothesis = 56
total_shares_premise = 300
total_shares_hypothesis = 300
average_price_premise = 40
average_price_hypothesis = 40

# the hypothesis refers to the prices of MicroTron and Dynaco stocks, the total number of shares sold, 
# and the average price per share mentioned in the premise
if microtron_stock_price_premise <= microtron_stock_price_hypothesis:
    # check if the 'microtron_stock_price_hypothesis' contradicts the microtron stock price in the premise
    label = "contradiction"
elif dynaco_stock_price_hypothesis != dynaco_stock_price_premise:
    # check if the dynaco stock price in the hypothesis contradicts the dynaco stock price reported in the premise
    label = "contradiction"
elif total_shares_hypothesis != total_shares_premise:
    # check if the total number of shares sold in the hypothesis contradicts the total number of shares sold in the premise
    label = "contradiction"
elif average_price_hypothesis != average_price_premise:
    # check if the average price per share in the hypothesis contradicts the average price per share in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

