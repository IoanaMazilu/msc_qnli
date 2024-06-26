ayisha_father_age_premise = 2 * shankar_age_premise
ayisha_father_age_hypothesis = 2 * shankar_age_hypothesis

# the hypothesis refers to the age of Ayisha's father and Shankar, mentioned in the premise
if ayisha_father_age_hypothesis <= ayisha_father_age_premise:
    # check if the estimate of 'ayisha_father_age_hypothesis' contradicts the age of Ayisha's father in the premise
    label = "contradiction"
elif shankar_age_hypothesis!= shankar_age_premise:
    # check if the age of Shankar in the hypothesis contradicts the age of Shankar reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
