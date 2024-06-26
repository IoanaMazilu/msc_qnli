# Define variables for the premise
microtron_price_premise = 36
dynaco_price_premise = 48
total_shares_premise = 300
average_price_premise = 40

# Define variables for the hypothesis
microtron_price_hypothesis = 76
dynaco_price_hypothesis = 48
total_shares_hypothesis = 300
average_price_hypothesis = 40

# Calculate the number of shares of Dynaco stock sold
dynaco_shares_sold_premise = total_shares_premise * (average_price_premise / microtron_price_premise)
dynaco_shares_sold_hypothesis = total_shares_hypothesis * (average_price_hypothesis / microtron_price_hypothesis)

# Check if the hypothesis values contradict the premise
if dynaco_shares_sold_hypothesis!= dynaco_shares_sold_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
