owners_premise = less_than_70
owners_hypothesis = 50

# the hypothesis refers to the number of owners in the city of San Durango
if owners_hypothesis <= owners_premise:
    # check if the hypothesis value contradicts the premise estimate
    label = "contradiction"
elif owners_hypothesis > owners_premise:
    # check if the hypothesis value entails the premise estimate
    label = "entailment"
else:
    # the premise gives only an estimate for the number of owners
    # any number of owners less than or equal to 70 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
