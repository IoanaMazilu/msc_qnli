father_age_premise = 0 # assume father's age is positive
ayisha_age_hypothesis = 1/6

# the hypothesis refers to a specific proportion of Ayisha's age compared to her father's age
if father_age_premise * ayisha_age_hypothesis <= father_age_premise:
    # check if the proportion in the hypothesis contradicts the proportion in the premise
    label = "contradiction"
else:
    # the premise gives a rough estimate of the proportion, but the hypothesis provides a more specific value
    label = "entailment"

print(label)
