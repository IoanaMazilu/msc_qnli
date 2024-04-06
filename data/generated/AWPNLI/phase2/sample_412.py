# Premise: Jessica had 8.0 quarters in her bank and her sister gave her 3.0 quarters.
# Hypothesis: Jessica has 11.0 quarters now.
# Golden Label: entailment

quarters_initial_premise = 8.0
quarters_received_premise = 3.0
total_quarters_hypothesis = 11.0

# the hypothesis refers to the total number of quarters, which also appear in the premise
# compute the total number of quarters from the premise
total_quarters_premise = quarters_initial_premise + quarters_received_premise
if total_quarters_hypothesis != total_quarters_premise:
    # check if the total number of quarters in the hypothesis contradicts the total number of quarters from the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

