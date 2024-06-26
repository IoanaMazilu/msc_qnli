jane_age_premise = 32
jane_age_hypothesis = 32
babysitting_stop_premise = 12
babysitting_stop_hypothesis = 12

# the hypothesis refers to Jane's age and the years since she stopped baby-sitting
if jane_age_hypothesis > jane_age_premise:
    # check if the hypothesis value contradicts the exact age of 'jane_age_premise'
    label = "contradiction"
elif babysitting_stop_hypothesis != babysitting_stop_premise:
    # check if the number of years since she stopped baby-sitting in the hypothesis contradicts the years reported in the premise
    label = "contradiction"
else:
    # the hypothesis values and estimates do not contradict the premise ones, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
