# Premise: Alyssa picked 42.0 pears from the pear tree and Nancy sold 17.0 of the pears.
# Hypothesis: 21.0 pears were left.
# Golden Label: contradiction

picked_pears_premise = 42.0
sold_pears_premise = 17.0
left_pears_hypothesis = 21.0

# the hypothesis refers to the number of pears left, which can be inferred from the premise
# compute the total number of pears left in the premise
left_pears_premise = picked_pears_premise - sold_pears_premise
if left_pears_hypothesis != left_pears_premise:
    # check if the number of pears left in the hypothesis contradicts the number of pears left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

