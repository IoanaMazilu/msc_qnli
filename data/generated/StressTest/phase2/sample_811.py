# Premise: Sacha runs at a constant speed of less than 7 meters per second, and Bruno runs at a constant speed of 5 meters per second.
# Hypothesis: Sacha runs at a constant speed of 6 meters per second, and Bruno runs at a constant speed of 5 meters per second.
# Golden Label: neutral

sacha_speed_premise = 7
sacha_speed_hypothesis = 6
bruno_speed_premise = 5
bruno_speed_hypothesis = 5

# the hypothesis talks about the speed of Sacha and Bruno, referenced also in the premise
if sacha_speed_hypothesis >= sacha_speed_premise:
    # check if the hypothesis value contradicts the estimate of less than 'sacha_speed_premise'
    label = "contradiction"
elif bruno_speed_hypothesis != bruno_speed_premise:
    # check if the speed of Bruno in the hypothesis contradicts the speed of Bruno reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of Sacha
    # any speed of Sacha less than 'sacha_speed_premise' and equal to 'bruno_speed_premise' is consistent with the premise,
    # but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

