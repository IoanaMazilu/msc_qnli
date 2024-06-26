subjects_premise = [45, 67, 76, 82, 85]
subjects_hypothesis = [55, 67, 76, 82, 85]

# the hypothesis refers to the number of subjects Reeya obtained grades in
if subjects_premise!= subjects_hypothesis:
    # check if the number of subjects in the hypothesis contradicts the number of subjects in the premise
    label = "contradiction"
else:
    # if the number of subjects in the hypothesis does not contradict the number of subjects in the premise, we can infer entailment
    label = "entailment"

print(label)
