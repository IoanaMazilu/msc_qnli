average_price_premise = 50
average_price_hypothesis = 40

# Both premise and hypothesis are questions asking the number of oranges to be put back to achieve certain average prices
if average_price_premise != average_price_hypothesis:
    # As the average price asked in the hypothesis does not match with the premise
    label = "contradiction"
else:
    # If the average prices in both premise and hypothesis were the same, it would be an entailment
    label = "entailment"

print(label)
