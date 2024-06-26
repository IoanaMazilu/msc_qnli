premise_microtron_price = 36
premise_dynaco_price = 48
premise_total_shares = 300
premise_average_price = 40

hypothesis_microtron_price = 76
hypothesis_dynaco_price = 48
hypothesis_total_shares = 300
hypothesis_average_price = 40

# calculate the total value of the shares sold
premise_total_value = premise_microtron_price * premise_total_shares + premise_dynaco_price * premise_total_shares
hypothesis_total_value = hypothesis_microtron_price * hypothesis_total_shares + hypothesis_dynaco_price * hypothesis_total_shares

# calculate the average price per share
premise_average_price = premise_total_value / premise_total_shares
hypothesis_average_price = hypothesis_total_value / hypothesis_total_shares

# check if the average price per share in the hypothesis contradicts the average price per share in the premise
if hypothesis_average_price <= premise_average_price:
    label = "contradiction"
else:
    label = "neutral"

print(label)
