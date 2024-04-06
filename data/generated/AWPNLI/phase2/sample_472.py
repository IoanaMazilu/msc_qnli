# Premise: Melanie picked 7.0 plums and 4.0 oranges from the orchard and Sam gave her 3.0 plums.
# Hypothesis: She has 10.0 plums now.
# Golden Label: entailment

picked_plums_premise = 7.0
given_plums_premise = 3.0
total_plums_hypothesis = 10.0

# the hypothesis refers to the total number of plums, which are also mentioned in the premise
# compute the total number of plums in the premise
total_plums_premise = picked_plums_premise + given_plums_premise
if total_plums_hypothesis != total_plums_premise:
    # check if the total number of plums in the hypothesis contradicts the total number of plums from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

