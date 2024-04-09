ayisha_age_fraction_premise = 1/6
ayisha_age_fraction_hypothesis = 3/6

# the hypothesis refers to Ayisha's age in relation to her father's age, also mentioned in the premise
if ayisha_age_fraction_hypothesis <= ayisha_age_fraction_premise:
    # check if the fraction of Ayisha's age in the hypothesis contradicts the fraction of Ayisha's age in the premise
    label = "contradiction"
else:
    # if the hypothesis fraction does not contradict the premise fraction, we can infer entailment
    label = "entailment"

print(label)
