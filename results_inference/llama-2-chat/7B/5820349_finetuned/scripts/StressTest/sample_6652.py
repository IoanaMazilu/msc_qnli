apples_maddie_premise = 88
apples_maddie_hypothesis = 18
apples_given_premise = 12
apples_given_hypothesis = 12

# the hypothesis talks about the number of apples Maddie has and the number of apples she gives to Mike
if apples_given_hypothesis!= apples_given_premise:
    # check if the number of apples given to Mike in the hypothesis contradicts the number of apples given to Mike in the premise
    label = "contradiction"
elif apples_maddie_hypothesis >= apples_maddie_premise:
    # check if the number of apples Maddie has left in the hypothesis contradicts the estimate of less than 'apples_maddie_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of apples Maddie has
    # any number of apples less than 'apples_maddie_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
