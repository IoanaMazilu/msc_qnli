# Premise: A 100-foot diameter asteroid will pass within 26,500 miles of Earth, the closest-ever brush on record by a space rock, NASA astronomers said.
# Hypothesis: An asteroid with a diameter of 100 feet will pass close by Earth, astronomers said.
# Golden Label: entailment

asteroid_diameter_premise = 100 # feet
asteroid_distance_premise = 26500 # miles
asteroid_diameter_hypothesis = 100 # feet

# the hypothesis talks about the size of the asteroid and the fact that it will pass close by Earth, without specifying the distance

if asteroid_diameter_premise != asteroid_diameter_hypothesis:
    # check if the size of the asteroid in the hypothesis contradicts the size in the premise
    label = "contradiction"
else:
    # if the size of the asteroid in the hypothesis does not contradict the size in the premise,
    # we can infer entailment, even if the distance in the premise is not specified in the hypothesis
    label = "entailment"

print(label)

