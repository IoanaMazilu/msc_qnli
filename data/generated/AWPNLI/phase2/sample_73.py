# Premise: Melanie picked 7.0 plums and 4.0 oranges from the orchard and she gave 3.0 plums to Sam.
# Hypothesis: She has 8.0 plums now.
# Golden Label: contradiction

picked_plums_premise = 7.0 
picked_oranges_premise = 4.0
given_plums_premise = 3.0
plums_hypothesis = 8.0

# the hypothesis refers to the number of plums, which are also mentioned in the premise
# compute the total number of plums in the premise
total_plums_premise = picked_plums_premise - given_plums_premise
if plums_hypothesis != total_plums_premise:
    # check if the number of plums in the hypothesis contradicts the number of plums from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

