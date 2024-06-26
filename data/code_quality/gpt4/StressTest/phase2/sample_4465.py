total_premise = 488
total_hypothesis = 288
proportions = [5, 7, 4, 8]

# We calculate the smallest parts in the premise and hypothesis by dividing the total by the sum of the proportions
# and then multiplying the result by the smallest proportion (which is 4).
smallest_part_premise = (total_premise / sum(proportions)) * min(proportions)
smallest_part_hypothesis = (total_hypothesis / sum(proportions)) * min(proportions)

# We are comparing the smallest parts in both premise and hypothesis
if smallest_part_premise != smallest_part_hypothesis:
    # If the smallest part in the premise is not equal to the smallest part in the hypothesis, we have a contradiction
    label = "contradiction"
else:
    # If the smallest parts are equal, we have an entailment
    label = "entailment"

print(label)
