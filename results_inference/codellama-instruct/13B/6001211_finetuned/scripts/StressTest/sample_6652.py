apples_maddie_premise = 88
apples_maddie_hypothesis = 18
apples_given = 12

# the hypothesis refers to the number of apples Maddie has, which is also mentioned in the premise
if apples_maddie_hypothesis >= apples_maddie_premise:
    # check if the number of apples Maddie has in the hypothesis contradicts the estimate of less than 'apples_maddie_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of apples Maddie has
    # any number of apples less than 'apples_maddie_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
