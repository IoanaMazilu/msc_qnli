# Premise: Two of the arrested cartel members were responsible for the payments for the killings, and two acted as lookouts during the incident, he said.
# Hypothesis: Two of the arrested were responsible for payout ; two acted as lookouts, official says.
# Golden Label: entailment

responsible_premise = 2
responsible_hypothesis = 2
lookouts_premise = 2
lookouts_hypothesis = 2

# the hypothesis mentions the number of arrested members responsible for payouts and acting as lookouts, which is also referenced in the premise
if responsible_hypothesis != responsible_premise:
    # check if the number of arrested responsible for payouts in the hypothesis contradicts the same number in the premise
    label = "contradiction"
elif lookouts_hypothesis != lookouts_premise:
    # check if the number of arrested acting as lookouts from the hypothesis contradicts the same number in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

