jane_age_premise = 40
jane_age_hypothesis = 20

# the hypothesis refers to the age when Jane started baby-sitting, mentioned in the premise
if jane_age_premise <= jane_age_hypothesis:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif jane_age_hypothesis < jane_age_premise:
    # check if the hypothesis value is consistent with the premise
    label = "neutral"
else:
    # the premise gives only an estimate for the age when Jane started baby-sitting
    # any age less than or equal to 20 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
