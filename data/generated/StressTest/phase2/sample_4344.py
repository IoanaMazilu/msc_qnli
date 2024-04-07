# Premise: While driving from City A to City B, Bob drives at a constant speed of 40 miles per hour.
# Hypothesis: While driving from City A to City B, Bob drives at a constant speed of more than 20 miles per hour.
# Golden Label: entailment

speed_premise = 40
speed_hypothesis = 20

# the hypothesis refers to the speed of Bob's drive from City A to City B, also mentioned in the premise
if speed_premise <= speed_hypothesis:
    # check if the speed in the premise contradicts the speed estimate in the hypothesis
    label = "contradiction"
else:
    # if the speed in the premise does not contradict the speed in the hypothesis, we can infer entailment
    label = "entailment"

print(label)

