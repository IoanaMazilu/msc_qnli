father_age_premise = 2 * shankar_age_premise + 10
father_age_hypothesis = 2 * shankar_age_hypothesis + 30

# the hypothesis refers to the future age of Ayisha's father, which is also mentioned in the premise
if father_age_hypothesis!= father_age_premise:
    # check if the future age of Ayisha's father in the hypothesis contradicts the future age reported in the premise
    label = "contradiction"
elif father_age_premise + 10!= father_age_hypothesis:
    # check if the age of Ayisha's father after 10 years in the hypothesis contradicts the age reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
