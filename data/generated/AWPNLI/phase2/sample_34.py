# Premise: Jessica had 8.0 quarters in her bank and her sister borrowed 3.0 of her quarters.
# Hypothesis: Jessica has 5.0 quarters now.
# Golden Label: entailment

quarters_initial_premise = 8.0
borrowed_quarters_premise = 3.0
quarters_hypothesis = 5.0

# the hypothesis refers to the number of quarters Jessica has now, which is also referenced in the premise
# compute the total number of quarters Jessica has now in the premise
total_quarters_premise = quarters_initial_premise - borrowed_quarters_premise
if quarters_hypothesis != total_quarters_premise:
    # check if the number of quarters in the hypothesis contradicts the number of quarters from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

