customers_without_power_premise = 2000
customers_without_power_hypothesis = 2000

# the hypothesis mentions the number of customers without power, which is also mentioned in the premise
if customers_without_power_hypothesis!= customers_without_power_premise:
    # check if the number of customers without power in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the number of customers without power in the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)
