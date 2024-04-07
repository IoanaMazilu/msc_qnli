# Premise: If the average speed of the whole journey was more than 16 mph, then what is Tom's speed driving from B to C in miles per hour?
# Hypothesis: If the average speed of the whole journey was 36 mph, then what is Tom's speed driving from B to C in miles per hour?
# Golden Label: neutral

average_speed_premise = 16
average_speed_hypothesis = 36

# the hypothesis refers to the average speed mentioned in the premise
if average_speed_hypothesis <= average_speed_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif average_speed_hypothesis > average_speed_premise:
    # the premise gives only an estimate for the average speed
    # any average speed greater than 'average_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

