# Premise: Emily has a cylindrical water bottle that can hold less than 6000 π cubic centimeters of water.
# Hypothesis: Emily has a cylindrical water bottle that can hold 1000 π cubic centimeters of water.
# Golden Label: neutral

import math

bottle_volume_premise = 6000 * math.pi
bottle_volume_hypothesis = 1000 * math.pi

# the hypothesis refers to the volume of the water bottle mentioned in the premise
if bottle_volume_hypothesis >= bottle_volume_premise:
    # check if the hypothesis value contradicts the estimate of less than 'bottle_volume_premise'
    label = "contradiction"
elif bottle_volume_hypothesis < bottle_volume_premise:
    # since the premise gives only an estimate for the volume of the bottle
    # any volume less than 'bottle_volume_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

