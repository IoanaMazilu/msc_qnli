# Premise: Jessica had 8.0 quarters in her bank and her sister gave her 3.0 quarters.
# Hypothesis: Jessica has 14.0 quarters now.
# Golden Label: contradiction

quarters_premise = 8.0
received_quarters_premise = 3.0
total_quarters_hypothesis = 14.0

# the hypothesis refers to the number of quarters, which are also mentioned in the premise
# compute the total number of quarters in the premise
total_quarters_premise = quarters_premise + received_quarters_premise
if total_quarters_hypothesis != total_quarters_premise:
    # check if the number of quarters in the hypothesis contradicts the number of quarters from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

