premise = "An investor can sell her MicroTron stock for less than 76 $per share and her Dynaco stock for 68 $per share, If she sells 300 shares altogether, some of each stock, at an average price per share of 40 $, how many shares of Dynaco stock has she sold?"
hypothesis = "An investor can sell her MicroTron stock for 36 $per share and her Dynaco stock for 68 $per share, If she sells 300 shares altogether, some of each stock, at an average price per share of 40 $, how many shares of Dynaco stock has she sold?"

# extract the numerical entities from the premise and hypothesis
premise_microtron_price = 76
premise_dynaco_price = 68
hypothesis_microtron_price = 36
hypothesis_dynaco_price = 68
premise_total_shares = 300
premise_average_price = 40

# calculate the total value of the stocks sold
premise_microtron_value = premise_microtron_price * premise_total_shares
premise_dynaco_value = premise_dynaco_price * premise_total_shares
hypothesis_microtron_value = hypothesis_microtron_price * premise_total_shares
hypothesis_dynaco_value = hypothesis_dynaco_price * premise_total_shares

# compare the total value of the stocks sold in the premise and hypothesis
if premise_microtron_value < hypothesis_microtron_value and premise_dynaco_value > hypothesis_dynaco_value:
    # the hypothesis contradicts the premise
    label = "contradiction"
elif premise_microtron_value > hypothesis_microtron_value and premise_dynaco_value < hypothesis_dynaco_value:
    # the hypothesis entails the premise
    label = "entailment"
else:
    # the hypothesis is neutral with respect to the premise
    label = "neutral"

print(label)
