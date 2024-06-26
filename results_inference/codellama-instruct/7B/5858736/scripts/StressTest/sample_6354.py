# Define variables for the premise
microtron_price = 36
dynaco_price = 48
total_shares = 300
average_price = 40

# Define variables for the hypothesis
microtron_price_hypothesis = 76
dynaco_price_hypothesis = 48

# Calculate the number of shares of Dynaco stock sold
dynaco_shares_sold = total_shares * (average_price / dynaco_price)

# Check if the hypothesis values contradict the premise
if microtron_price_hypothesis > microtron_price:
    label = "contradiction"
elif dynaco_price_hypothesis!= dynaco_price:
    label = "contradiction"
elif dynaco_shares_sold!= total_shares:
    label = "contradiction"
else:
    label = "entailment"

print(label)
