# Premise: Ed drives at a constant speed of 31 km per hour.
# Hypothesis: Ed drives at a constant speed of less than 31 km per hour.
# Golden Label: contradiction

speed_premise = 31
speed_hypothesis = 31

# the hypothesis refers to the same speed value as the premise
if speed_hypothesis < speed_premise:
    # check if the hypothesis value contradicts the premise value of 'speed_premise'
    label = "contradiction"
elif speed_hypothesis == speed_premise:
    # check if the hypothesis value can be entailed from the premise value of 'speed_premise'
    label = "entailment"
else:
    # if the hypothesis value neither contradicts nor can be entailed from the premise value, then it's neutral
    label = "neutral"

print(label)

