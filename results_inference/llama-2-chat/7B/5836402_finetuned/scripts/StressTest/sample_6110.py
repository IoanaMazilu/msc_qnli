level_graduates_premise = 15
level_graduates_hypothesis = 15

# the hypothesis refers to the level of graduates in Amtek's sales staff, which is also mentioned in the premise
if level_graduates_hypothesis <= level_graduates_premise:
    # check if the hypothesis value contradicts the estimate of more than 'level_graduates_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the level of graduates
    # any level of graduates greater than 'level_graduates_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
