gloves_premise = 20
gloves_hypothesis = 60

# the hypothesis refers to the number of gloves Andy has, which is also mentioned in the premise
if gloves_hypothesis <= gloves_premise:
    # check if the hypothesis value contradicts the estimate of more than 'gloves_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of gloves
    # any number of gloves greater than 'gloves_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
