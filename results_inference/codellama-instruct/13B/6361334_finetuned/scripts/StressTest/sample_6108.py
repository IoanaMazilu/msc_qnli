college_graduates_premise = 15
college_graduates_hypothesis = 4

# the hypothesis refers to the number of college graduates in Amtek's sales staff, mentioned in the premise
if college_graduates_hypothesis >= college_graduates_premise:
    # check if the hypothesis value contradicts the number of college graduates in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the number of college graduates
    # any number of college graduates less than 'college_graduates_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
