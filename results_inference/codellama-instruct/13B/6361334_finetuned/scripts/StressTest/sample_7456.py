apples_maddie_premise = 18
apples_maddie_hypothesis = 48
apples_mike_premise = 22
apples_mike_hypothesis = 22

# the hypothesis refers to the number of apples Maddie has and the number of apples she gives to Mike
# the premise mentions the number of apples Maddie has and the number of apples she gives to Mike
# the hypothesis value contradicts the premise value for the number of apples Maddie has
if apples_maddie_hypothesis!= apples_maddie_premise:
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of apples Maddie has
    # any number of apples greater than 'apples_maddie_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
