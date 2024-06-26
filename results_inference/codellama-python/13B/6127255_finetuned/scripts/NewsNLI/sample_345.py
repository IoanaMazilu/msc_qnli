deceased_families_premise = 12
victims_families_premise = 5
amount_premise = 220000

deceased_families_hypothesis = 12
victims_families_hypothesis = 5
amount_hypothesis = 220000

# the hypothesis mentions the number of deceased and disabled families and the amount that will be distributed to them, which are also mentioned in the premise
if deceased_families_hypothesis!= deceased_families_premise:
    # check if the number of deceased families in the hypothesis contradicts the number of deceased families reported in the premise
    label = "contradiction"
elif victims_families_hypothesis!= victims_families_premise:
    # check if the number of disabled families from the hypothesis contradicts the number of disabled families in the premise
    label = "contradiction"
elif amount_hypothesis!= amount_premise:
    # check if the amount in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
