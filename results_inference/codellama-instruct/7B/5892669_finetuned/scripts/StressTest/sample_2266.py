gloves_premise = 60
gloves_hypothesis = 20

# the hypothesis talks about the number of pairs of gloves Andy has, referenced also in the premise
if gloves_hypothesis >= gloves_premise:
    # check if the hypothesis value contradicts the estimate of less than 'gloves_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of gloves
    # any number of gloves less than 'gloves_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
