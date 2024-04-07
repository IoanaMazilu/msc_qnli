# Premise: Store Z:$90, a 20% sales tax, and $10 rebate after tax Isaac can purchase a certain item in four different ways, as shown in the table.
# Hypothesis: Store Z:$more than 60, a 20% sales tax, and $10 rebate after tax Isaac can purchase a certain item in four different ways, as shown in the table.
# Golden Label: entailment

store_z_price_premise = 90
store_z_price_hypothesis = 60

# the hypothesis talks about the price of an item in store Z, which is also mentioned in the premise
if store_z_price_premise <= store_z_price_hypothesis:
    # check if the hypothesis contradicts the premise by suggesting a lower price for the item
    label = "contradiction"
elif store_z_price_hypothesis != store_z_price_premise:
    # check if the price suggested in the hypothesis contradicts the exact price mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

