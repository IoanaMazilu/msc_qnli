# Premise: Steve gets on the elevator at the less than 51 th floor of a building and rides up at a rate of 87 floors per minute.
# Hypothesis: Steve gets on the elevator at the 11 th floor of a building and rides up at a rate of 87 floors per minute.
# Golden Label: neutral

initial_floor_premise = 51
initial_floor_hypothesis = 11
rate_per_minute_premise = 87
rate_per_minute_hypothesis = 87

# the hypothesis talks about the initial floor and the rate per minute, both also mentioned in the premise

if initial_floor_hypothesis >= initial_floor_premise:
    # check if the initial floor in the hypothesis contradicts the premise of it being less than 'initial_floor_premise'
    label = "contradiction"
elif rate_per_minute_hypothesis != rate_per_minute_premise:
    # check if the rate per minute in the hypothesis contradicts the rate per minute mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

