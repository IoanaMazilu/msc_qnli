sun_brightness_premise = 1000
sun_brightness_hypothesis = 100

# the hypothesis states that the sun is 100 times brighter than the moon
if sun_brightness_hypothesis <= sun_brightness_premise:
    # check if the hypothesis value contradicts the estimate of more than'sun_brightness_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the sun's brightness
    # any number of brightness greater than'sun_brightness_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
