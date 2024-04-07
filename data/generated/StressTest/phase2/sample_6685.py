# Premise: Vinod climbs less than 80 steps in 40 seconds.
# Hypothesis: Vinod climbs 60 steps in 40 seconds.
# Golden Label: neutral

steps_premise = 80
steps_hypothesis = 60

# the hypothesis talks about the number of steps climbed by Vinod, referenced also in the premise
if steps_hypothesis >= steps_premise:
    # check if the hypothesis value contradicts the estimate of less than 'steps_premise'
    label = "contradiction"
elif steps_hypothesis < steps_premise:
    # any number of steps less than 'steps_premise' is consistent with the premise and can be entailed from the premise
    label = "entailment"

print(label)

