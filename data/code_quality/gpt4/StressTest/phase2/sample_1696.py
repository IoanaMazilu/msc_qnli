jane_age_premise = 12
jane_age_hypothesis = 32
years_stopped_babysitting_premise = 10
years_stopped_babysitting_hypothesis = 10

# the hypothesis refers to Jane's age and the number of years she stopped babysitting as mentioned in the premise
if jane_age_hypothesis <= jane_age_premise:
    # check if the 'jane_age_hypothesis' contradicts the premise that Jane is more than 12 years old
    label = "contradiction"
elif years_stopped_babysitting_hypothesis != years_stopped_babysitting_premise:
    # check if the number of years Jane stopped babysitting in the hypothesis contradicts the number of years reported in the premise
    label = "contradiction"
else:
    # the premise gives only a minimum for Jane's age,
    # thus, any age greater than 'jane_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
