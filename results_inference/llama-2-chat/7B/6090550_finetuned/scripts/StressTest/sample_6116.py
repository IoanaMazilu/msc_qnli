micro_tron_price_premise = 36
dynaco_price_premise = 68
total_shares_premise = 300
average_price_premise = 40

micro_tron_price_hypothesis = 36
dynaco_price_hypothesis = 68
total_shares_hypothesis = 300
average_price_hypothesis = 40

# the hypothesis talks about the price and the number of shares sold for both stocks, which are also mentioned in the premise
if micro_tron_price_hypothesis!= micro_tron_price_premise or dynaco_price_hypothesis!= dynaco_price_premise:
    # check if the price of either stock in the hypothesis contradicts the price reported in the premise
    label = "contradiction"
elif total_shares_hypothesis!= total_shares_premise or average_price_hypothesis!= average_price_premise:
    # check if the number of shares sold or the average price per share in the hypothesis contradicts the information in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
