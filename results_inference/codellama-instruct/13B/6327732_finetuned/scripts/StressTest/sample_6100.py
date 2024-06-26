days_premise = 86
days_hypothesis = 16

# the hypothesis refers to the number of days it will take for Mary to complete a certain task alone
if days_hypothesis >= days_premise:
    # check if the hypothesis value contradicts the estimate of less than 'days_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the number of days it will take for Mary to complete a certain task alone
    # any number of days less than 'days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
