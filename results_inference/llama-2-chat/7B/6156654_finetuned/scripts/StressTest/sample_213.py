average_speed_whole_journey_premise = 36
average_speed_whole_journey_hypothesis = 76

# the hypothesis refers to the average speed of the whole journey, which is also mentioned in the premise
if average_speed_whole_journey_hypothesis <= average_speed_whole_journey_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, it can be entailed from the premise
    label = "entailment"

print(label)
