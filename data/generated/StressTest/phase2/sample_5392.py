# Premise: Alice drives at a constant speed of less than 40 km per hour.
# Hypothesis: Alice drives at a constant speed of 30 km per hour.
# Golden Label: neutral

speed_premise = 40
speed_hypothesis = 30

# the hypothesis refers to Alice's driving speed mentioned in the premise
if speed_hypothesis >= speed_premise:
    # check if the speed in the hypothesis contradicts the estimate of less than 'speed_premise'
    label = "contradiction"
elif speed_hypothesis < speed_premise:
    # if the speed in the hypothesis is less than 'speed_premise', it is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

