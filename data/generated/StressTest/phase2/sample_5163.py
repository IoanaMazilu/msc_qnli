# Premise: On her way back, Venki drives 45 miles per hour and stops in Town Y which is midway between Town X and Town Z.
# Hypothesis: On her way back, Venki drives more than 25 miles per hour and stops in Town Y which is midway between Town X and Town Z.
# Golden Label: entailment

driving_speed_premise = 45
driving_speed_hypothesis = 25

# the hypothesis refers to the driving speed and stopping point mentioned in the premise
if driving_speed_premise <= driving_speed_hypothesis:
    # check if the estimate of 'driving_speed_hypothesis' contradicts the driving speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

