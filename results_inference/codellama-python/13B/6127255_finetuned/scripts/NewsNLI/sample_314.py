money_transport_premise = 10000
money_transport_hypothesis = 10000

# the hypothesis mentions the amount of money that must be declared, which is also mentioned in the premise
if money_transport_hypothesis!= money_transport_premise:
    # check if the amount of money in the hypothesis contradicts the amount of money in the premise
    label = "contradiction"
else:
    # if the amount of money in the hypothesis does not contradict the amount of money in the premise, we can infer entailment
    label = "entailment"

print(label)
