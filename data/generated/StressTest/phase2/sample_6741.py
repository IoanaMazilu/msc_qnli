# Premise: While driving from City A to City B, Ed drives at a constant speed of 30 miles per hour.
# Hypothesis: While driving from City A to City B, Ed drives at a constant speed of more than 20 miles per hour.
# Golden Label: entailment

speed_premise = 30
speed_hypothesis = 20

# the hypothesis talks about the speed of Ed while driving, which is also mentioned in the premise
if speed_hypothesis >= speed_premise:
    # check if the hypothesis value contradicts the constant speed of 'speed_premise' mentioned in the premise
    label = "contradiction"
else:
    # if the speed in the hypothesis is less than the speed in the premise, it is consistent with the premise and can be explicitly entailed
    label = "entailment"

print(label)

