# Premise: David can divide his herd into 5 equal parts and also to 6 equal parts, but not to 9 equal parts.
# Hypothesis: David can divide his herd into more than 5 equal parts and also to 6 equal parts, but not to 9 equal parts.
# Golden Label: contradiction

herd_parts_premise = 5
herd_parts_hypothesis = 5
herd_parts_premise_2 = 6
herd_parts_hypothesis_2 = 6
herd_parts_premise_3 = 9
herd_parts_hypothesis_3 = 9

# the hypothesis refers to the same conditions of dividing the herd as the premise
if herd_parts_hypothesis != herd_parts_premise:
    # check if the number of equal parts in the hypothesis contradicts the number of equal parts in the premise
    label = "contradiction"
elif herd_parts_hypothesis_2 != herd_parts_premise_2:
    # check if the number of equal parts in the hypothesis contradicts the number of equal parts in the premise
    label = "contradiction"
elif herd_parts_hypothesis_3 != herd_parts_premise_3:
    # check if the hypothesis contradicts the premise about not being able to divide the herd into 'herd_parts_hypothesis_3' equal parts
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

