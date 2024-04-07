# Premise: Glen drives at a constant speed of less than 67 km per hour.
# Hypothesis: Glen drives at a constant speed of 37 km per hour.
# Golden Label: neutral

speed_premise = 67
speed_hypothesis = 37

# the hypothesis provides a specific speed at which Glen drives, while the premise gives an upper limit
if speed_hypothesis >= speed_premise:
    # check if the speed in the hypothesis contradicts the premise's upper limit
    label = "contradiction"
elif speed_hypothesis < speed_premise:
    # the premise gives only an upper limit for the speed
    # any speed less than 'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

