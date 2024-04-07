# Premise: At the same time Jose gets on an elevator on the less than 61 st floor of the same building and rides down at a rate of 63 floors per minute.
# Hypothesis: At the same time Jose gets on an elevator on the 51 st floor of the same building and rides down at a rate of 63 floors per minute.
# Golden Label: neutral

floor_premise = 61
floor_hypothesis = 51
rate_premise = 63
rate_hypothesis = 63

# the hypothesis refers to the floor number and rate of descent mentioned in the premise
if floor_hypothesis >= floor_premise:
    # check if the hypothesis floor number contradicts the premise estimate of less than 'floor_premise'
    label = "contradiction"
elif rate_hypothesis != rate_premise:
    # check if the rate of descent in the hypothesis contradicts the rate of descent mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

