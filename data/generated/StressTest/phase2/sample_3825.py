# Premise: David can divide his herd into 5 equal parts and also to 6 equal parts, but not to 9 equal parts.
# Hypothesis: David can divide his herd into more than 3 equal parts and also to 6 equal parts, but not to 9 equal parts.
# Golden Label: entailment

herd_parts_premise_1 = 5
herd_parts_premise_2 = 6
herd_parts_premise_3 = 9
herd_parts_hypothesis_1 = 3
herd_parts_hypothesis_2 = 6
herd_parts_hypothesis_3 = 9

# the hypothesis refers to the equal parts David can divide his herd into, also mentioned in the premise
if herd_parts_premise_1 <= herd_parts_hypothesis_1 or herd_parts_premise_2 != herd_parts_hypothesis_2 or herd_parts_premise_3 != herd_parts_hypothesis_3:
    # check if the estimates of 'herd_parts_hypothesis' contradict the numbers in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

