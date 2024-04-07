# Premise: If Martin returned two packet to the retailer, and the average price of the remaining millk packet was 12 ¢, then what is the average price, in cents, of the two returned milk packets?
# Hypothesis: If Martin returned two packet to the retailer, and the average price of the remaining millk packet was less than 12 ¢, then what is the average price, in cents, of the two returned milk packets?
# Golden Label: contradiction

avg_price_remaining_premise = 12
avg_price_remaining_hypothesis = 12

# the hypothesis refers to the average price of the remaining milk packets mentioned in the premise
if avg_price_remaining_hypothesis != avg_price_remaining_premise:
    # check if the average price mentioned in the hypothesis contradicts the average price stated in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

