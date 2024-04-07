# Premise: An investor can sell her MicroTron stock for 36 $per share and her Dynaco stock for 48 $per share, If she sells 300 shares altogether, some of each stock, at an average price per share of 40 $, how many shares of Dynaco stock has she sold?
# Hypothesis: An investor can sell her MicroTron stock for 76 $per share and her Dynaco stock for 48 $per share, If she sells 300 shares altogether, some of each stock, at an average price per share of 40 $, how many shares of Dynaco stock has she sold?
# Golden Label: contradiction

microtron_price_premise = 36
microtron_price_hypothesis = 76
dynaco_price_premise = 48
dynaco_price_hypothesis = 48
total_shares_premise = 300
total_shares_hypothesis = 300
average_price_premise = 40
average_price_hypothesis = 40

# the hypothesis refers to the price per share of MicroTron and Dynaco stocks, the total number of shares sold, and average price per share, mentioned in the premise
if microtron_price_premise != microtron_price_hypothesis:
    # check if the price per share of MicroTron stock in the hypothesis contradicts the price per share of MicroTron stock in the premise
    label = "contradiction"
elif dynaco_price_premise != dynaco_price_hypothesis:
    # check if the price per share of Dynaco stock in the hypothesis contradicts the price per share of Dynaco stock in the premise
    label = "contradiction"
elif total_shares_premise != total_shares_hypothesis:
    # check if the total number of shares sold in the hypothesis contradicts the total number of shares sold in the premise
    label = "contradiction"
elif average_price_premise != average_price_hypothesis:
    # check if the average price per share in the hypothesis contradicts the average price per share in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

