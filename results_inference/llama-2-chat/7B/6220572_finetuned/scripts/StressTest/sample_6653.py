apples_premise = 18
apples_hypothesis = 58
given_apples_premise = 12
given_apples_hypothesis = 12

# the hypothesis talks about the number of apples Maddie has and the number of apples she gives to Mike
if apples_hypothesis == apples_premise:
    # check if the number of apples in the hypothesis contradicts the number of apples in the premise
    label = "contradiction"
elif given_apples_hypothesis!= given_apples_premise:
    # check if the number of apples Maddie gives to Mike in the hypothesis contradicts the number of apples given in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of apples
    # any number of apples consistent with the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
