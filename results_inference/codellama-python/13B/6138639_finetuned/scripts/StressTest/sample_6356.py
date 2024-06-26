microtron_price_premise = 36
dynaco_price_premise = 48
total_shares_premise = 300
average_price_premise = 40

microtron_price_hypothesis = 76
dynaco_price_hypothesis = 48
total_shares_hypothesis = 300
average_price_hypothesis = 40

# the hypothesis talks about the price of MicroTron and Dynaco stocks, referenced also in the premise
if microtron_price_hypothesis!= microtron_price_premise:
    # check if the price of MicroTron stock in the hypothesis contradicts the price of MicroTron stock in the premise
    label = "contradiction"
elif dynaco_price_hypothesis!= dynaco_price_premise:
    # check if the price of Dynaco stock in the hypothesis contradicts the price of Dynaco stock in the premise
    label = "contradiction"
elif total_shares_hypothesis!= total_shares_premise:
    # check if the total number of shares in the hypothesis contradicts the total number of shares in the premise
    label = "contradiction"
elif average_price_hypothesis!= average_price_premise:
    # check if the average price per share in the hypothesis contradicts the average price per share in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
