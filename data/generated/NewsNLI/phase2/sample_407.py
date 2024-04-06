# Premise: A paper trail found suspect payments in Mexico totaled more than $24 million, the newspaper said, citing an internal Wal-Mart review.
# Hypothesis: An internal review found suspect payments totaling more than $24 million, the report says.
# Golden Label: entailment

suspect_payments_premise = 24000000
suspect_payments_hypothesis = 24000000

# the hypothesis mentions the amount of suspect payments, which is also mentioned in the premise
if suspect_payments_hypothesis != suspect_payments_premise:
    # check if the suspect payments amount in the hypothesis contradicts the suspect payments reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

