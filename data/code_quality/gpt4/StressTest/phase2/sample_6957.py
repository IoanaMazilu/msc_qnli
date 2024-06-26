toys_purchased_premise = 20 # dozens
toys_purchased_hypothesis = 20 # dozens
rate_per_dozen_premise = 375
rate_per_dozen_hypothesis = 275

# the hypothesis refers to the number of dozens of toys purchased and the rate per dozen mentioned in the premise
if toys_purchased_premise != toys_purchased_hypothesis:
    # check if the number of dozens of toys purchased in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif rate_per_dozen_premise <= rate_per_dozen_hypothesis:
    # check if the rate per dozen in the hypothesis contradicts the rate per dozen reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
