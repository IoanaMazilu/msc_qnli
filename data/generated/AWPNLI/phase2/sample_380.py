# Premise: Sara has 31.0 red and 15.0 green balloons and she gave Sandy 24.0 red balloons.
# Hypothesis: She has 7.0 red balloons left.
# Golden Label: entailment

red_balloons_premise = 31.0
green_balloons_premise = 15.0
given_red_balloons_premise = 24.0
red_balloons_left_hypothesis = 7.0

# the hypothesis refers to the number of red balloons left, which can be computed from the premise
# compute the number of red balloons left in the premise
red_balloons_left_premise = red_balloons_premise - given_red_balloons_premise
if red_balloons_left_hypothesis != red_balloons_left_premise:
    # check if the number of red balloons left in hypothesis contradicts the number of red balloons left from the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"   

print(label)

