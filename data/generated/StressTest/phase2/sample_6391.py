# Premise: Sacha runs at a constant speed of more than 1 meters per second, and Bruno runs at a constant speed of 5 meters per second.
# Hypothesis: Sacha runs at a constant speed of 6 meters per second, and Bruno runs at a constant speed of 5 meters per second.
# Golden Label: neutral

sacha_speed_premise = 1
sacha_speed_hypothesis = 6
bruno_speed_premise = 5
bruno_speed_hypothesis = 5

# the hypothesis refers to the speeds of Sacha and Bruno mentioned in the premise
if sacha_speed_hypothesis <= sacha_speed_premise:
    # check if the speed of Sacha in the hypothesis contradicts the premise
    label = "contradiction"
elif bruno_speed_hypothesis != bruno_speed_premise:
    # check if the speed of Bruno in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of Sacha, any speed greater than 'sacha_speed_premise' is consistent with the premise
    # the speed of Bruno in the hypothesis matches the speed of Bruno in the premise
    label = "neutral"

print(label)

