apples_premise = 460
apples_hypothesis = 360

# the hypothesis refers to the number of apples Anita has, also mentioned in the premise
if apples_hypothesis >= apples_premise:
    # check if the hypothesis value contradicts the estimate of less than 'apples_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of apples
    # any number of apples less than 'apples_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)