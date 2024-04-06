# Premise: Sara had 21.0 quarters in her bank and her dad gave her 49.0 more quarters.
# Hypothesis: She has 70.0 quarters now.
# Golden Label: entailment

quarters_bank_premise = 21.0
quarters_dad_premise = 49.0
total_quarters_hypothesis = 70.0

# the hypothesis refers to the total number of quarters, which are also mentioned in the premise
# compute the total number of quarters in the premise
total_quarters_premise = quarters_bank_premise + quarters_dad_premise
if total_quarters_hypothesis != total_quarters_premise:
    # check if the total number of quarters in the hypothesis contradicts the total number of quarters from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

