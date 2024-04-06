# Premise: Sara had 100.0 pennies and 783.0 quarters in her bank and her dad gave 271.0 quarters to Sara.
# Hypothesis: She has 1049.0 quarters now.
# Golden Label: contradiction

pennies_premise = 100.0
quarters_premise = 783.0
quarters_given_premise = 271.0
quarters_hypothesis = 1049.0

# the hypothesis refers to the number of quarters, which is also mentioned in the premise
# compute the total number of quarters in the premise
total_quarters_premise = quarters_premise + quarters_given_premise
if quarters_hypothesis != total_quarters_premise:
    # check if the number of quarters in the hypothesis contradicts the number of quarters from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

