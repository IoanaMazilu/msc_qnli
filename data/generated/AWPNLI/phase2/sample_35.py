# Premise: Jessica had 8.0 quarters in her bank and her sister borrowed 3.0 of her quarters.
# Hypothesis: Jessica has 2.0 quarters now.
# Golden Label: contradiction

quarters_premise = 8.0
borrowed_quarters_premise = 3.0
quarters_hypothesis = 2.0

# the hypothesis refers to the number of quarters Jessica has now, which can be computed from the premise
# compute the total number of quarters Jessica has now in the premise
remaining_quarters_premise = quarters_premise - borrowed_quarters_premise
if quarters_hypothesis != remaining_quarters_premise:
    # check if the number of quarters in the hypothesis contradicts the number of quarters Jessica has now from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

