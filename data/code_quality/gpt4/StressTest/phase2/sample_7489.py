apples_premise = 460
apples_hypothesis = 360

# the hypothesis refers to the number of apples Anita has, similarly mentioned in the premise
if apples_hypothesis >= apples_premise:
    # check if the hypothesis contradicts the estimate of less than 'apples_premise'
    label = "contradiction"
else:
    # if the hypothesis value is consistent with the premise but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
