reading_rate_premise = 7
reading_rate_hypothesis = 5

# the hypothesis and the premise both refer to the reading rate of Jose
if reading_rate_hypothesis >= reading_rate_premise:
    # check if the reading rate in the hypothesis contradicts the premise
    label = "contradiction"
elif reading_rate_hypothesis < reading_rate_premise:
    # if the reading rate in the hypothesis is less than that in the premise, it implies entailment
    label = "entailment"

print(label)
