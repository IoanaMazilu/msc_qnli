# Premise: An investor can sell her MicroTron stock for less than 76 $per share and her Dynaco stock for 68 $per share, If she sells 300 shares altogether, some of each stock, at an average price per share of 40 $, how many shares of Dynaco stock has she sold?
# Hypothesis: An investor can sell her MicroTron stock for 36 $per share and her Dynaco stock for 68 $per share, If she sells 300 shares altogether, some of each stock, at an average price per share of 40 $, how many shares of Dynaco stock has she sold?
# Golden Label: neutral

microtron_price_premise = 76
dynaco_price_premise = 68
total_shares_premise = 300
average_price_premise = 40

microtron_price_hypothesis = 36
dynaco_price_hypothesis = 68
total_shares_hypothesis = 300
average_price_hypothesis = 40

# the hypothesis refers to the prices per share and total shares sold mentioned in the premise
if microtron_price_hypothesis >= microtron_price_premise:
    # check if the 'microtron_price_hypothesis' contradicts the price per share in the premise
    label = "contradiction"
elif dynaco_price_hypothesis != dynaco_price_premise:
    # check if the 'dynaco_price_hypothesis' contradicts the price per share in the premise
    label = "contradiction"
elif total_shares_hypothesis != total_shares_premise:
    # check if the 'total_shares_hypothesis' contradicts the total shares sold in the premise
    label = "contradiction"
elif average_price_hypothesis != average_price_premise:
    # check if the 'average_price_hypothesis' contradicts the average price per share in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

