# Premise: Eleven individuals and eight policemen were injured, two seriously, the official Algerie Presse Service reported.
# Hypothesis: 11 individuals, 8 police injured, Algeria's official news agency reports.
# Golden Label: entailment

individuals_injured_premise = 11
policemen_injured_premise = 8

individuals_injured_hypothesis = 11
policemen_injured_hypothesis = 8

# the hypothesis mentions the number of injured individuals and policemen, which are also mentioned in the premise
if individuals_injured_hypothesis != individuals_injured_premise:
    # check if the number of injured individuals in the hypothesis contradicts the number in the premise
    label = "contradiction"
elif policemen_injured_hypothesis != policemen_injured_premise:
    # check if the number of injured policemen from the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

