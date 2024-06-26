packets_milk_premise = 5
packets_milk_hypothesis = 2
average_price_premise = 20
average_price_hypothesis = 20

# the hypothesis refers to the number of milk packets and their average price mentioned in the premise
if packets_milk_premise <= packets_milk_hypothesis:
    # check if the estimate of 'packets_milk_hypothesis' contradicts the number of milk packets bought in the premise
    label = "contradiction"
elif average_price_hypothesis != average_price_premise:
    # check if the average price in the hypothesis contradicts the average price reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
