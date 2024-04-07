# Premise: At the same time Jose gets on an elevator on the 51 st floor of the same building and rides down at a rate of 63 floors per minute.
# Hypothesis: At the same time Jose gets on an elevator on the 31 st floor of the same building and rides down at a rate of 63 floors per minute.
# Golden Label: contradiction

floor_start_premise = 51
floor_start_hypothesis = 31
rate_premise = 63
rate_hypothesis = 63

# the hypothesis refers to the situation described in the premise
if floor_start_premise != floor_start_hypothesis:
    # check if the starting floor in the hypothesis contradicts the starting floor reported in the premise
    label = "contradiction"
elif rate_premise != rate_hypothesis:
    # check if the rate of descending in the hypothesis contradicts the rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)

