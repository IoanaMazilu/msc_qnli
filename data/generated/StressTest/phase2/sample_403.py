# Premise: Sacha runs at a constant speed of more than 5 meters per second, and Bruno runs at a constant speed of 5 meters per second.
# Hypothesis: Sacha runs at a constant speed of 6 meters per second, and Bruno runs at a constant speed of 5 meters per second.
# Golden Label: neutral

sacha_speed_premise = 5
sacha_speed_hypothesis = 6
bruno_speed_premise = 5
bruno_speed_hypothesis = 5

# the hypothesis talks about the speeds of Sacha and Bruno, both also mentioned in the premise
if sacha_speed_hypothesis <= sacha_speed_premise:
    # check if Sacha's speed in the hypothesis contradicts the estimate of more than 'sacha_speed_premise'
    label = "contradiction"
elif bruno_speed_hypothesis != bruno_speed_premise:
    # check if Bruno's speed in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only a lower bound for Sacha's speed
    # any speed for Sacha greater than 'sacha_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
