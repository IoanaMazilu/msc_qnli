premise = "An investor can sell her MicroTron stock for 36 $per share and her Dynaco stock for 48 $per share, If she sells 300 shares altogether, some of each stock, at an average price per share of 40 $, how many shares of Dynaco stock has she sold?"
hypothesis = "An investor can sell her MicroTron stock for less than 76 $per share and her Dynaco stock for 48 $per share, If she sells 300 shares altogether, some of each stock, at an average price per share of 40 $, how many shares of Dynaco stock has she sold?"

# extract the numerical entities from the premise and hypothesis
premise_microtron_price = 36
premise_dynaco_price = 48
hypothesis_microtron_price = 76
hypothesis_dynaco_price = 48
premise_total_shares = 300
premise_average_price = 40

# calculate the total value of the stocks sold
premise_microtron_value = premise_microtron_price * premise_total_shares
premise_dynaco_value = premise_dynaco_price * premise_total_shares

# calculate the total value of the stocks sold at the average price
premise_average_microtron_value = premise_microtron_price * premise_total_shares / premise_average_price
premise_average_dynaco_value = premise_dynaco_price * premise_total_shares / premise_average_price

# calculate the number of shares of Dynaco stock sold
premise_dynaco_shares = premise_dynaco_value / premise_dynaco_price

# compare the number of shares of Dynaco stock sold in the premise and hypothesis
if premise_dynaco_shares <= hypothesis_dynaco_shares:
    # check if the hypothesis value contradicts the number of shares of Dynaco stock sold in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of shares of Dynaco stock sold
    # any number of shares greater than 'premise_dynaco_shares' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
