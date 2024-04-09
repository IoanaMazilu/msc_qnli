london_eye_premise = 443
high_roller_premise = 550
rosy_match_premise = "Rosy also matched the London Eye and Las Vegas’High Roller"

# define variables for the numerical entities in the premise
london_eye_hypothesis = float(rosy_match_hypothesis.split(" ")[1])
high_roller_hypothesis = float(rosy_match_hypothesis.split(" ")[2])

# compare the values of the numerical entities in the premise and hypothesis
if london_eye_hypothesis < london_eye_premise:
    # the hypothesis contradicts the premise
    label = "contradiction"
elif high_roller_hypothesis < high_roller_premise:
    # the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the hypothesis values are consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
