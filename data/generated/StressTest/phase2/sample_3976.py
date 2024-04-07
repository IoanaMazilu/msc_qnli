# Premise: Carl drove from his home to the beach at an average speed of more than 70 kilometers per hour and returned home by the same route at an average speed of 70 kilometers per hour.
# Hypothesis: Carl drove from his home to the beach at an average speed of 80 kilometers per hour and returned home by the same route at an average speed of 70 kilometers per hour.
# Golden Label: neutral

average_speed_premise = 70
average_speed_hypothesis = 80
return_speed_premise = 70
return_speed_hypothesis = 70

# the hypothesis talks about the average speed Carl drove and returned home, referenced also in the premise
if average_speed_hypothesis <= average_speed_premise:
    # check if the hypothesis value contradicts the estimate of more than 'average_speed_premise'
    label = "contradiction"
elif return_speed_hypothesis != return_speed_premise:
    # check if the return speed in the hypothesis contradicts the return speed reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average speed
    # any speed greater than 'average_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

