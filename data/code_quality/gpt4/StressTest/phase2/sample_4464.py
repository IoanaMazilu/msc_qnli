total_premise = 288
total_hypothesis = 488
proportions = [5, 7, 4, 8]

# calculate the smallest part for premise and hypothesis
smallest_part_premise = (min(proportions) / sum(proportions)) * total_premise
smallest_part_hypothesis = (min(proportions) / sum(proportions)) * total_hypothesis

# the hypothesis refers to the way of dividing a number (in this case less than 488) into four parts proportional to 5, 7, 4, 8
# the smallest part of this division is compared with the smallest part of a similar division for the number 288
if smallest_part_hypothesis >= smallest_part_premise:
    # check if the hypothesis smallest part contradicts the premise smallest part
    label = "contradiction"
else:
    # the premise gives only a specific value for the total to be divided
    # any total less than 'total_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
