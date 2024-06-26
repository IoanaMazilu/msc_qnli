owners_premise = 50
owners_hypothesis = 75

# the hypothesis refers to the number of owners in the city
if owners_hypothesis <= owners_premise:
    # check if the hypothesis value contradicts the estimate of 'owners_premise'
    label = "contradiction"
elif owners_hypothesis > owners_premise:
    # check if the hypothesis value entails the premise
    label = "entailment"
else:
    # the premise gives only an estimate for the number of owners
    # any number of owners greater than 'owners_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
