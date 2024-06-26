graduates_premise = 10
graduates_hypothesis = 7

# the hypothesis refers to the number of college graduates in Listco's sales staff, mentioned in the premise
if graduates_hypothesis >= graduates_premise:
    # check if the hypothesis value contradicts the number of college graduates in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the number of college graduates in Listco's sales staff
    # any number of college graduates less than 'graduates_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
