# Premise: Find the area of a rectangular field if John walking at the speed of 48 m/min took 20 seconds to cross the field diagonally and Harry walking at a speed of 72 m/min took 15 seconds to cross the field along its sides.
# Hypothesis: Find the area of a rectangular field if John walking at the speed of more than 48 m/min took 20 seconds to cross the field diagonally and Harry walking at a speed of 72 m/min took 15 seconds to cross the field along its sides.
# Golden Label: contradiction

john_speed_premise = 48
john_speed_hypothesis = 48
harry_speed_premise = 72
harry_speed_hypothesis = 72

# the hypothesis refers to the speed of John and Harry when crossing the field, which is also mentioned in the premise
if john_speed_hypothesis <= john_speed_premise:
    # check if the hypothesis value contradicts the estimate of more than 'john_speed_premise'
    label = "contradiction"
elif harry_speed_hypothesis != harry_speed_premise:
    # check if the speed of Harry in the hypothesis contradicts the speed of Harry reported in the premise
    label = "contradiction"
else:
    # the premise gives exact speed for John and Harry
    # any speed of John greater than 'john_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

