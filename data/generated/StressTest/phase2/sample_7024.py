# Premise: While driving from City A to City B, Cara drives at a constant speed of less than 80 miles per hour.
# Hypothesis: While driving from City A to City B, Cara drives at a constant speed of 30 miles per hour.
# Golden Label: neutral

speed_premise = 80
speed_hypothesis = 30

# the hypothesis discusses about the driving speed from City A to City B, which is also mentioned in the premise
if speed_hypothesis >= speed_premise:
    # check if the hypothesis speed contradicts the premise of less than 'speed_premise'
    label = "contradiction"
elif speed_hypothesis < speed_premise:
    # if the hypothesis speed is less than 'speed_premise', it is consistent with the premise
    # but the premise does not provide enough information to explicitly entail the hypothesis
    label = "neutral"

print(label)

