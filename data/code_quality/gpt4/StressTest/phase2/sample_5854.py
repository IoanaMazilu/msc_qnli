dolls_bought_premise = 3
dolls_bought_hypothesis = 5
nieces_premise = 5
nieces_hypothesis = 5

# the hypothesis refers to the number of dolls bought and nieces mentioned in the premise
if dolls_bought_hypothesis <= dolls_bought_premise:
    # check if the hypothesis value contradicts the estimate of more than 'dolls_bought_premise'
    label = "contradiction"
elif nieces_hypothesis != nieces_premise:
    # check if the number of nieces in the hypothesis contradicts the number of nieces in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of dolls
    # any number of dolls greater than 'dolls_bought_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
