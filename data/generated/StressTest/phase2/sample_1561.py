# Premise: If Martin returned two packet to the retailer, and the average price of the remaining millk packet was less than 32 ¢, then what is the average price, in cents, of the two returned milk packets?
# Hypothesis: If Martin returned two packet to the retailer, and the average price of the remaining millk packet was 12 ¢, then what is the average price, in cents, of the two returned milk packets?
# Golden Label: neutral

avg_price_premise = 32
avg_price_hypothesis = 12

# the hypothesis talks about the average price of the remaining milk packets, which is also mentioned in the premise
if avg_price_hypothesis >= avg_price_premise:
    # check if the hypothesis value contradicts the statement of less than 'avg_price_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the average price 
    # a lower average price is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

