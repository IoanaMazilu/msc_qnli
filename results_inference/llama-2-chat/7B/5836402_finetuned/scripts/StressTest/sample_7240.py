ayisha_age_premise = 1/6
ayisha_age_hypothesis = 1/6
father_age_premise = 3/6

# the hypothesis refers to Ayisha's age and her father's age mentioned in the premise
if ayisha_age_hypothesis!= ayisha_age_premise:
    # check if the age of Ayisha in the hypothesis contradicts the age of Ayisha reported in the premise
    label = "contradiction"
elif father_age_hypothesis!= father_age_premise:
    # check if the age of Ayisha's father in the hypothesis contradicts the age of Ayisha's father reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
