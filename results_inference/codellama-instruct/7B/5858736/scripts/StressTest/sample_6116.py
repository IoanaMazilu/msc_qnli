# Define variables for the premise
microtron_price = 36
dynaco_price = 68
total_shares = 300
average_price = 40

# Define variables for the hypothesis
microtron_price_hypothesis = 36
dynaco_price_hypothesis = 68
total_shares_hypothesis = 300
average_price_hypothesis = 40

# Calculate the number of shares of Dynaco stock sold
dynaco_shares_sold = total_shares_hypothesis * (dynaco_price_hypothesis / average_price_hypothesis)

# Check if the hypothesis values contradict the premise
if microtron_price_hypothesis > microtron_price:
    label = "contradiction"
elif dynaco_price_hypothesis < dynaco_price:
    label = "contradiction"
elif total_shares_hypothesis!= total_shares:
    label = "contradiction"
elif average_price_hypothesis!= average_price:
    label = "contradiction"
else:
    label = "entailment"

print(label)
