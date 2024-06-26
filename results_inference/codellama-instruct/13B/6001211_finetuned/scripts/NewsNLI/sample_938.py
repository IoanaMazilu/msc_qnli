parts_manufactured_premise = 0.8
parts_manufactured_hypothesis = 0.8

# the hypothesis mentions the percentage of parts manufactured in the U.S., which is also mentioned in the premise
if parts_manufactured_hypothesis <= parts_manufactured_premise:
    # check if the percentage of parts manufactured in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis percentage does not contradict the premise percentage, we can infer neutrality
    label = "neutral"

print(label)
