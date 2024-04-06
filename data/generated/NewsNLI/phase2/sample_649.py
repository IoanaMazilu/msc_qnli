# Premise: Stern's attorney, Lin Wood, told CNN the suit seeks $10 million for compensatory damages and $50 million for punitive damages.
# Hypothesis: Howard K. Stern's lawsuit seeks $60 million in damages.
# Golden Label: neutral

compensatory_damages_premise = 10e6
punitive_damages_premise = 50e6
total_damages_premise = compensatory_damages_premise + punitive_damages_premise

total_damages_hypothesis = 60e6

# the hypothesis mentions the total amount sought in Stern's lawsuit, which can be obtained by adding the compensatory and punitive damages from the premise
if total_damages_hypothesis != total_damages_premise:
    # check if the total amount in the hypothesis contradicts the total amount calculated from the premise
    label = "contradiction"
else:
    # if the total amount from the hypothesis matches the total amount calculated from the premise, we can infer entailment
    label = "entailment"

print(label)

