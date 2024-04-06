# Premise: San Diego Gas and Electric said all of its 1.4 million customers were without power.
# Hypothesis: San Diego-area utility says 1.4 million customers are without power.
# Golden Label: entailment

customers_without_power_premise = 1.4e6
customers_without_power_hypothesis = 1.4e6

# the hypothesis mentions the number of customers without power, which is also referenced in the premise
if customers_without_power_hypothesis != customers_without_power_premise:
    # check if the number of customers without power in the hypothesis contradicts the number stated in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)

