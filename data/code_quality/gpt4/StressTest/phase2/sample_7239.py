ayisha_age_fraction_premise = 1/6
ayisha_age_fraction_hypothesis = 3/6

# the hypothesis refers to the fraction of Ayisha's age compared to her father's age, mentioned in the premise
if ayisha_age_fraction_hypothesis <= ayisha_age_fraction_premise:
    # check if the fraction of Ayisha's age to her father's age in the hypothesis contradicts the fraction in the premise
    label = "contradiction"
elif ayisha_age_fraction_hypothesis > ayisha_age_fraction_premise:
    # the hypothesis fraction is greater than the premise fraction, hence cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis fraction does not contradict the premise fraction, we can infer entailment
    label = "entailment"

print(label)
