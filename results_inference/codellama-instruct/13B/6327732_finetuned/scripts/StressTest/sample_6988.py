age_anil_premise = 2
age_son_premise = 3
age_anil_hypothesis = 7
age_son_hypothesis = 3

# the hypothesis refers to the ratio of the ages of Anil and his son at present
if age_anil_hypothesis / age_son_hypothesis <= age_anil_premise / age_son_premise:
    # check if the estimate of 'age_anil_hypothesis' contradicts the ratio of ages in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of the ages
    # any ratio greater than 'age_anil_premise / age_son_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
