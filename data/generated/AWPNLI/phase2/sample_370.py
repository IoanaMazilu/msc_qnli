# Premise: Melanie had 7.0 dimes in her bank and her dad gave her 8.0 dimes, and she gave her mother 4.0 dimes.
# Hypothesis: Melanie has 11.0 dimes now.
# Golden Label: entailment

dimes_melanie_premise = 7.0
dimes_dad_premise = 8.0
dimes_mother_premise = 4.0
dimes_now_hypothesis = 11.0

# the hypothesis refers to the number of dimes Melanie has now, which can be computed from the premise
# compute the total number of dimes Melanie has now according to the premise
dimes_now_premise = dimes_melanie_premise + dimes_dad_premise - dimes_mother_premise
if dimes_now_hypothesis != dimes_now_premise:
    # check if the number of dimes in the hypothesis contradicts the number of dimes from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

