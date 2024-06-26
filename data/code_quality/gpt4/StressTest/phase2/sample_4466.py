total_premise = 288
smallest_part_premise_proportion = 4
total_parts_proportions_premise = 5 + 7 + 4 + 8
smallest_part_premise = (smallest_part_premise_proportion / total_parts_proportions_premise) * total_premise

total_hypothesis = total_premise - 1 # as it is less than 288
total_parts_proportions_hypothesis = 5 + 7 + 4 + 8
smallest_part_hypothesis = (smallest_part_premise_proportion / total_parts_proportions_hypothesis) * total_hypothesis

# the hypothesis talks about the smallest part resulting from a division, similar to the premise
if smallest_part_hypothesis != smallest_part_premise:
    # check if the smallest part in the hypothesis contradicts the smallest part in the premise
    label = "contradiction"
else:
    # the premise gives a specific value for the smallest part
    # if the hypothesis smallest part is the same, then we can infer entailment
    label = "entailment"

print(label)
