# Premise: An investor can sell her MicroTron stock for less than 66 $per share and her Dynaco stock for 44 $per share, If she sells 300 shares altogether, some of each stock, at an average price per share of 40 $, how many shares of Dynaco stock has she sold?
# Hypothesis: An investor can sell her MicroTron stock for 36 $per share and her Dynaco stock for 44 $per share, If she sells 300 shares altogether, some of each stock, at an average price per share of 40 $, how many shares of Dynaco stock has she sold?
# Golden Label: neutral

microtron_price_premise = 66
microtron_price_hypothesis = 36
dynaco_price_premise = 44
dynaco_price_hypothesis = 44
total_shares_premise = 300
total_shares_hypothesis = 300
average_price_premise = 40
average_price_hypothesis = 40

# the hypothesis refers to the prices of the MicroTron and Dynaco stocks, the total number of sold shares and the average price per share mentioned in the premise
if microtron_price_hypothesis >= microtron_price_premise:
    # check if the price of MicroTron stock in the hypothesis contradicts the price of MicroTron stock in the premise
    label = "contradiction"
elif dynaco_price_hypothesis != dynaco_price_premise or total_shares_hypothesis != total_shares_premise or average_price_hypothesis != average_price_premise:
    # check if the price of Dynaco stock, the total number of sold shares or the average price per share in the hypothesis contradicts the ones reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

