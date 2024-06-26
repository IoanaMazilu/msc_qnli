demonstrators_injured_premise = 2
officers_injured_premise = 2
total_injured_premise = demonstrators_injured_premise + officers_injured_premise

total_injured_hypothesis = 4
officers_injured_hypothesis = 2

# we first check if the total number of injured people in the hypothesis is the same as the sum of the injured demonstrators and officers in the premise
if total_injured_hypothesis != total_injured_premise:
    label = "contradiction"
# additionally, we verify if the number of injured officers in the hypothesis matches the one in the premise
elif officers_injured_hypothesis != officers_injured_premise:
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
