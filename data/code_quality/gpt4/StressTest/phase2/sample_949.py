apples_billy_premise = 72
apples_billy_hypothesis = 12

# the hypothesis talks about the number of apples Billy has, which is also referenced in the premise
if apples_billy_hypothesis >= apples_billy_premise:
    # check if the number of apples in the hypothesis contradicts the premise of having less than 'apples_billy_premise' apples
    label = "contradiction"
else:
    # any number of apples less than 'apples_billy_premise' is consistent with the premise, but it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
