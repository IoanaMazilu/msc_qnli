percentage_premise = 0.09
percentage_hypothesis = 0.09

# the hypothesis mentions the percentage of people who would like to time travel, which is also mentioned in the premise
if percentage_hypothesis!= percentage_premise:
    # check if the percentage in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis value and the premise value are the same, we can infer neutrality
    label = "neutral"

print(label)
