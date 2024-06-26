# Define variables for the numerical entities in the premise and hypothesis
microtron_stock_premise = 76
dynaco_stock_premise = 48
total_shares_premise = 300
average_price_premise = 40

microtron_stock_hypothesis = 36
dynaco_stock_hypothesis = 48

# Calculate the number of shares of Dynaco stock sold
dynaco_shares_sold = (total_shares_premise * average_price_premise) / (microtron_stock_premise + dynaco_stock_premise)

# Check if the hypothesis values contradict the premise
if microtron_stock_hypothesis!= microtron_stock_premise:
    label = "contradiction"
elif dynaco_stock_hypothesis!= dynaco_stock_premise:
    label = "contradiction"
elif dynaco_shares_sold!= total_shares_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
