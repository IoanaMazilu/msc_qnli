# Premise: If Pinky returned four chocolate to the retailer, and the average price of the remaining chocolate was 2 ¢, then what is the average price, in cents, of the four returned chocolates?
# Hypothesis: If Pinky returned four chocolate to the retailer, and the average price of the remaining chocolate was less than 4 ¢, then what is the average price, in cents, of the four returned chocolates?
# Golden Label: entailment

avg_price_premise = 2
avg_price_hypothesis = 4

# The hypothesis refers to the average price of the remaining chocolates mentioned in the premise
if avg_price_premise >= avg_price_hypothesis:
    # Check if the average price of remaining chocolates in the hypothesis contradicts the average price reported in the premise
    label = "contradiction"
else:
    # If the hypothesis average price does not contradict the premise average price, we can infer entailment
    label = "entailment"

print(label)

