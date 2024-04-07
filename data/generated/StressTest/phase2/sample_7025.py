# Premise: While driving from City A to City B, Cara drives at a constant speed of 30 miles per hour.
# Hypothesis: While driving from City A to City B, Cara drives at a constant speed of 10 miles per hour.
# Golden Label: contradiction

speed_premise = 30
speed_hypothesis = 10

# the hypothesis refers to the driving speed from City A to City B mentioned in the premise
if speed_premise != speed_hypothesis:
    # check if the driving speed in the hypothesis contradicts the driving speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

