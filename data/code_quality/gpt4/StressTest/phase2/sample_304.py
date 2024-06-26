sunil_age_difference_premise = 2
sunil_age_difference_hypothesis = 4

# the hypothesis talks about the age difference between Sunil and Syam, referenced also in the premise
if sunil_age_difference_hypothesis <= sunil_age_difference_premise:
    # check if the hypothesis value contradicts the estimate of more than 'sunil_age_difference_premise'
    label = "contradiction"
elif sunil_age_difference_hypothesis > sunil_age_difference_premise:
    # the premise gives only an estimate for the age difference
    # any age difference greater than 'sunil_age_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
