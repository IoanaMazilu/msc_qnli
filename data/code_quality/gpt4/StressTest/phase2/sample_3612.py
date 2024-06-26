# Defining variables
microtron_price_premise = 36
dynaco_price_premise = 60
total_shares_premise = 300
average_price_premise = 40

microtron_price_hypothesis = 56
dynaco_price_hypothesis = 60
total_shares_hypothesis = 300
average_price_hypothesis = 40

# Checking the prices of the stocks in the premise and the hypothesis
if microtron_price_premise >= microtron_price_hypothesis:
    label = "contradiction"
# Checking the total shares sold in the premise and the hypothesis
elif total_shares_premise != total_shares_hypothesis:
    label = "contradiction"
# Checking the average price per share in the premise and the hypothesis
elif average_price_premise != average_price_hypothesis:
    label = "contradiction"
else:
    # If all the conditions in the hypothesis are met in the premise, we can infer entailment
    label = "entailment"

print(label)
