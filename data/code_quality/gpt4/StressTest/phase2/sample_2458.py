lindy_speed_premise = 60
lindy_speed_hypothesis = 10

# the hypothesis refers to the speed of Lindy, which is also mentioned in the premise
if lindy_speed_hypothesis >= lindy_speed_premise:
    # check if the speed in the hypothesis contradicts the premise
    label = "contradiction"
elif lindy_speed_hypothesis < lindy_speed_premise:
    # if the speed in the hypothesis is less than the speed in the premise, this is consistent with the premise
    # but we cannot explicitly infer the specific speed mentioned in the hypothesis from the premise
    label = "neutral"
else:
    # an unexpected case, not covered by the above conditions
    label = "unknown"

print(label)
