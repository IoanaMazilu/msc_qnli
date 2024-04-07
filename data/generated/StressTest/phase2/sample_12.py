# Premise: On his way back, John drives 85 miles per hour and stops in Town Y which is midway between Town X and Town Z.
# Hypothesis: On his way back, John drives more than 65 miles per hour and stops in Town Y which is midway between Town X and Town Z.
# Golden Label: entailment

speed_premise = 85
speed_hypothesis = 65

# the hypothesis refers to the speed and the place where John stops which are mentioned in the premise
if speed_premise <= speed_hypothesis:
    # check if the speed in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
else:
    # if the speed in the hypothesis doesn't contradict the speed in the premise, we can infer entailment
    label = "entailment"

print(label)

