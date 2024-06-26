microtron_premise = 36
microtron_hypothesis = 76
dynaco_premise = 48
dynaco_hypothesis = 48
total_shares_premise = 300
total_shares_hypothesis = 300
avg_price_premise = 40
avg_price_hypothesis = 40

# the hypothesis talks about the price of MicroTron and Dynaco stocks, which are also mentioned in the premise
if microtron_hypothesis!= microtron_premise:
    # check if the price of MicroTron stock in the hypothesis contradicts the price in the premise
    label = "contradiction"
elif dynaco_hypothesis!= dynaco_premise:
    # check if the price of Dynaco stock in the hypothesis contradicts the price in the premise
    label = "contradiction"
elif total_shares_hypothesis!= total_shares_premise:
    # check if the total number of shares sold in the hypothesis contradicts the total number of shares sold in the premise
    label = "contradiction"
elif avg_price_hypothesis!= avg_price_premise:
    # check if the average price per share in the hypothesis contradicts the average price per share in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
