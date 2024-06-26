peanut_butter_premise = 152
peanut_butter_hypothesis = 252

# the hypothesis refers to the amount of peanut butter Jeff has, which is also mentioned in the premise
if peanut_butter_hypothesis <= peanut_butter_premise:
    # check if the amount of peanut butter in the hypothesis contradicts the premise of having more than 'peanut_butter_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of peanut butter
    # any quantity of peanut butter greater than 'peanut_butter_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
