parts_premise = 0.8
parts_hypothesis = 0.8

# the hypothesis mentions the percentage of parts made in the U.S., which is also mentioned in the premise
if parts_hypothesis!= parts_premise:
    # check if the percentage of parts made in the U.S. in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is the same as the premise value, we can infer neutrality
    label = "neutral"

print(label)
