# Premise: Sacha runs at a constant speed of more than 4 meters per second, and Bruno runs at a constant speed of 5 meters per second.
# Hypothesis: Sacha runs at a constant speed of 6 meters per second, and Bruno runs at a constant speed of 5 meters per second.
# Golden Label: neutral

sacha_speed_premise = 4
bruno_speed_premise = 5
sacha_speed_hypothesis = 6
bruno_speed_hypothesis = 5

# the hypothesis talks about the speeds of Sacha and Bruno, which are also referenced in the premise
if sacha_speed_hypothesis <= sacha_speed_premise:
    # check if the hypothesis speed for Sacha contradicts the premise that she runs faster than 'sacha_speed_premise'
    label = "contradiction"
elif bruno_speed_hypothesis != bruno_speed_premise:
    # check if the speed of Bruno in the hypothesis contradicts the speed of Bruno in the premise
    label = "contradiction"
elif sacha_speed_hypothesis > sacha_speed_premise and bruno_speed_hypothesis == bruno_speed_premise:
    # any speed of Sacha greater than 'sacha_speed_premise' is consistent with the premise,
    # but cannot be explicitly entailed from the premise. Also, Bruno's speed matches in both the premise and hypothesis.
    label = "neutral"

print(label)

