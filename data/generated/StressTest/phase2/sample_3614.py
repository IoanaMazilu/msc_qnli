# Premise: An investor can sell her MicroTron stock for 36 $per share and her Dynaco stock for 60 $per share, If she sells 300 shares altogether, some of each stock, at an average price per share of 40 $, how many shares of Dynaco stock has she sold?
# Hypothesis: An investor can sell her MicroTron stock for less than 36 $per share and her Dynaco stock for 60 $per share, If she sells 300 shares altogether, some of each stock, at an average price per share of 40 $, how many shares of Dynaco stock has she sold?
# Golden Label: contradiction

microtron_price_premise = 36
microtron_price_hypothesis = 36
dynaco_price_premise = 60
dynaco_price_hypothesis = 60
total_shares_premise = 300
total_shares_hypothesis = 300
average_price_premise = 40
average_price_hypothesis = 40

# the hypothesis refers to the prices per share of MicroTron and Dynaco stocks, the total shares sold and their average price per share
# these values are also mentioned in the premise
if microtron_price_hypothesis >= microtron_price_premise:
    # check if the hypothesis value for MicroTron's price contradicts the premise
    label = "contradiction"
elif dynaco_price_hypothesis != dynaco_price_premise:
    # check if Dynaco's price per share in the hypothesis contradicts the premise
    label = "contradiction"
elif total_shares_hypothesis != total_shares_premise:
    # check if the total number of shares sold in the hypothesis contradicts the premise
    label = "contradiction"
elif average_price_hypothesis != average_price_premise:
    # check if the average price per share in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

