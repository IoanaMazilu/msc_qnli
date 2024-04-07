# Premise: Vinod climbs 60 steps in 40 seconds.
# Hypothesis: Vinod climbs less than 80 steps in 40 seconds.
# Golden Label: entailment

steps_climbed_premise = 60
seconds_premise = 40
steps_climbed_hypothesis = 80
seconds_hypothesis = 40

# the hypothesis refers to the number of steps Vinod climbs in a certain time, also mentioned in the premise
if steps_climbed_premise >= steps_climbed_hypothesis:
    # check if the number of steps climbed in the premise contradicts the estimate of less than 'steps_climbed_hypothesis'
    label = "contradiction"
elif seconds_hypothesis != seconds_premise:
    # check if the time in the hypothesis contradicts the time mentioned in the premise
    label = "contradiction"
else:
    # if the values in the hypothesis do not contradict the ones in the premise, we can infer entailment
    label = "entailment"

print(label)

