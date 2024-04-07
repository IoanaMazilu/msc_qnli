# Premise: What is the average speed of Murali from A to C given that the ratio of distances between A to B and B to C is less than 3:3?
# Hypothesis: What is the average speed of Murali from A to C given that the ratio of distances between A to B and B to C is 2:3?
# Golden Label: neutral

ratio_premise = 3/3
ratio_hypothesis = 2/3

# the hypothesis refers to a specific ratio between the distances A to B and B to C, also mentioned in the premise
if ratio_hypothesis >= ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio less than 'ratio_premise' in the premise
    label = "contradiction"
elif ratio_hypothesis == ratio_premise:
    # if the hypothesis ratio equals the premise ratio, we infer entailment
    label = "entailment"
else:
    # the premise provides an upper limit for the ratio, but does not specify it
    # any ratio less than 'ratio_premise' does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

