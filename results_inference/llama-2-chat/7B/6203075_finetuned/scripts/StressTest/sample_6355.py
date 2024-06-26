# Defining the stock prices in the premise and hypothesis
micro_tron_price_premise = 76
dynaco_price_premise = 48
micro_tron_price_hypothesis = 36
dynaco_price_hypothesis = 48

# Defining the total number of shares sold in both cases
total_shares_sold_premise = 300
total_shares_sold_hypothesis = 300

# Calculating the average price per share in both cases
average_price_premise = (micro_tron_price_premise + dynaco_price_premise) / 2
average_price_hypothesis = (micro_tron_price_hypothesis + dynaco_price_hypothesis) / 2

# Comparing the average prices in both cases
if average_price_premise!= average_price_hypothesis:
    # If the average prices are not equal, then it's a contradiction
    label = "contradiction"
else:
    # If the average prices are equal, then it's an entailment
    label = "entailment"

print(label)
