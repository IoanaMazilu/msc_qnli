ayisha_age_premise = 1/6
ayisha_age_hypothesis = 1/6
father_age_premise = 1
father_age_hypothesis = 1

# the hypothesis refers to the fraction of Ayisha's and her father's ages mentioned in the premise
if ayisha_age_hypothesis >= ayisha_age_premise:
    # check if the fraction of Ayisha's age in the hypothesis contradicts the fraction of Ayisha's age in the premise
    label = "contradiction"
elif father_age_hypothesis!= father_age_premise:
    # check if the fraction of the father's age in the hypothesis contradicts the fraction of the father's age in the premise
    label = "contradiction"
else:
    # if the hypothesis fractions do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
