chip_speed_premise = 4  # GHz
chip_speed_hypothesis = 4  # gigahertz

# the hypothesis talks about the speed of the chip, which is also mentioned in the premise
if chip_speed_hypothesis <= chip_speed_premise:
    # check if the speed of the chip in the hypothesis contradicts the speed mentioned in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we cannot infer entailment
    label = "neutral"

print(label)
