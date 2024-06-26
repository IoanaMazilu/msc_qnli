premise = "An investor can sell her MicroTron stock for less than 76 $per share and her Dynaco stock for 48 $per share, If she sells 300 shares altogether, some of each stock, at an average price per share of 40 $, how many shares of Dynaco stock has she sold?"
hypothesis = "An investor can sell her MicroTron stock for 36 $per share and her Dynaco stock for 48 $per share, If she sells 300 shares altogether, some of each stock, at an average price per share of 40 $, how many shares of Dynaco stock has she sold?"

# extract the numerical entities from the premise and hypothesis
premise_microtron_price = 76
premise_dynaco_price = 48
hypothesis_microtron_price = 36
hypothesis_dynaco_price = 48
premise_total_shares = 300
premise_average_price = 40

# calculate the number of shares of Dynaco stock sold based on the premise
premise_dynaco_shares = premise_total_shares * premise_dynaco_price / premise_average_price

# calculate the number of shares of Dynaco stock sold based on the hypothesis
hypothesis_dynaco_shares = premise_total_shares * hypothesis_dynaco_price / premise_average_price

# compare the number of shares of Dynaco stock sold based on the premise and hypothesis
if hypothesis_dynaco_shares > premise_dynaco_shares:
    label = "contradiction"
elif hypothesis_dynaco_shares < premise_dynaco_shares:
    label = "entailment"
else:
    label = "neutral"

print(label)
