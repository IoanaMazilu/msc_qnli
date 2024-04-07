# Premise: Martin bought more than 2 packet milk at an average price (arithmetic mean) of 20 ¢.
# Hypothesis: Martin bought 5 packet milk at an average price (arithmetic mean) of 20 ¢.
# Golden Label: neutral

packet_milk_premise = 2
packet_milk_hypothesis = 5

# the hypothesis discusses about the number of packet milk bought by Martin, also referenced in the premise
if packet_milk_hypothesis <= packet_milk_premise:
    # check if the hypothesis value contradicts the estimate of more than 'packet_milk_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of packet milk
    # any number of packets greater than 'packet_milk_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

