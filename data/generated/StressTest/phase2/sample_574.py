# Premise: What is the average speed of Murali from A to C given that the ratio of distances between A to B and B to C is less than 30:5?
# Hypothesis: What is the average speed of Murali from A to C given that the ratio of distances between A to B and B to C is 10:5?
# Golden Label: neutral

ratio_premise = 30/5
ratio_hypothesis = 10/5

# the hypothesis talks about the ratio of distances between A to B and B to C, referenced also in the premise
if ratio_hypothesis >= ratio_premise:
    # check if the ratio value in hypothesis contradicts the estimate of less than 'ratio_premise'
    label = "contradiction"
elif ratio_hypothesis < ratio_premise:
    # the premise gives only an estimate for the ratio
    # any ratio less than 'ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

