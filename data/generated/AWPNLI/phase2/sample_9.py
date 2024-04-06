# Premise: Melanie had 7.0 dimes in her bank and her dad gave her 8.0 dimes, and her mother gave her 4.0 dimes.
# Hypothesis: Melanie has 18.0 dimes now.
# Golden Label: contradiction

dimes_melanie_premise = 7.0
dimes_dad_premise = 8.0
dimes_mother_premise = 4.0
total_dimes_hypothesis = 18.0

# the hypothesis refers to the total number of dimes, which are also mentioned in the premise
# compute the total number of dimes in the premise
total_dimes_premise = dimes_melanie_premise + dimes_dad_premise + dimes_mother_premise
if total_dimes_hypothesis != total_dimes_premise:
    # check if the total number of dimes in the hypothesis contradicts the total number of dimes from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

