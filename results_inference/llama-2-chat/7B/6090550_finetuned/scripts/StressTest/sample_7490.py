y = 560

anita_apples_premise = 360

# the hypothesis states the number of apples Anita has, which is also mentioned in the premise
if anita_apples_hypothesis == anita_apples_premise:
    # check if the number of apples in the hypothesis matches the number of apples in the premise
    label = "entailment"
else:
    # if the hypothesis value doesn't match the premise value, it's a contradiction
    label = "contradiction"

print(label)
