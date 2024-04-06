# Premise: Sara had 21.0 quarters in her bank and her dad gave her 49.0 more quarters.
# Hypothesis: She has 68.0 quarters now.
# Golden Label: contradiction

quarters_bank_premise = 21.0
quarters_given_premise = 49.0
total_quarters_hypothesis = 68.0

# the hypothesis refers to the total number of quarters, which are also mentioned in the premise
# compute the total number of quarters in the premise
total_quarters_premise = quarters_bank_premise + quarters_given_premise
if total_quarters_hypothesis != total_quarters_premise:
    # check if the total quarters in the hypothesis contradicts the total quarters from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

