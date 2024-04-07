# Premise: Steve gets on the elevator at the 11 th floor of a building and rides up at a rate of 47 floors per minute.
# Hypothesis: Steve gets on the elevator at the less than 81 th floor of a building and rides up at a rate of 47 floors per minute.
# Golden Label: entailment

starting_floor_premise = 11
starting_floor_hypothesis = 81
rate_premise = 47
rate_hypothesis = 47

# the hypothesis refers to the starting floor and rate of the elevator ride mentioned in the premise
if starting_floor_hypothesis <= starting_floor_premise:
    # check if the hypothesis value contradicts the 'starting_floor_premise'
    label = "contradiction"
elif rate_hypothesis != rate_premise:
    # check if the rate in the hypothesis contradicts the rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

