mary_age_diff_premise = 24
mary_age_diff_hypothesis = 14

# the hypothesis refers to the age difference between Mary and Albert mentioned in the premise
if mary_age_diff_hypothesis >= mary_age_diff_premise:
    # check if the age difference in the hypothesis contradicts the premise of Mary being 'mary_age_diff_premise' years younger than Albert
    label = "contradiction"
elif mary_age_diff_hypothesis < mary_age_diff_premise:
    # if the age difference in the hypothesis is less than 'mary_age_diff_premise', it does not contradict the premise, but it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
