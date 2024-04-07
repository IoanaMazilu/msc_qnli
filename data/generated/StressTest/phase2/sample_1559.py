# Premise: Martin bought 5 packet milk at an average price (arithmetic mean) of 20 ¢.
# Hypothesis: Martin bought 7 packet milk at an average price (arithmetic mean) of 20 ¢.
# Golden Label: contradiction

packets_premise = 5
packets_hypothesis = 7
average_price_premise = 20
average_price_hypothesis = 20

# the hypothesis refers to the number of milk packets Martin bought and their average price, both mentioned in the premise
if packets_premise != packets_hypothesis:
    # check if the number of packets in the hypothesis contradicts the number of packets reported in the premise
    label = "contradiction"
elif average_price_premise != average_price_hypothesis:
    # check if the average price in the hypothesis contradicts the average price reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

