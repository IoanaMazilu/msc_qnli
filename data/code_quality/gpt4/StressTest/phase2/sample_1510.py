cathy_stretch_premise = 57
cathy_stretch_hypothesis = 27

# the hypothesis refers to the time it takes Cathy to stretch, which is also mentioned in the premise
if cathy_stretch_hypothesis >= cathy_stretch_premise:
    # check if the 'cathy_stretch_hypothesis' contradicts the restriction of less than 'cathy_stretch_premise'
    label = "contradiction"
elif cathy_stretch_hypothesis < cathy_stretch_premise:
    # if the hypothesis value is less than the premise value, it does not contradict the premise
    # but it cannot be explicitly entailed from the premise either
    label = "neutral"

print(label)
