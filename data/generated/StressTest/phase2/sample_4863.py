# Premise: Mary is 8 years younger than Albert.
# Hypothesis: Mary is more than 1 years younger than Albert.
# Golden Label: entailment

mary_age_difference_premise = 8
mary_age_difference_hypothesis = 1

# the hypothesis talks about the age difference between Mary and Albert, referenced also in the premise
if mary_age_difference_hypothesis >= mary_age_difference_premise:
    # check if the hypothesis value contradicts the premise of Mary being 'mary_age_difference_premise' years younger than Albert
    label = "contradiction"
else:
    # the premise gives the exact age difference between Mary and Albert
    # any age difference less than 'mary_age_difference_premise' is consistent with the premise and can be explicitly entailed from the premise
    label = "entailment"

print(label)

