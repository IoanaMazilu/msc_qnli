subjects_premise = [50, 60, 70, 80, 80]
subjects_hypothesis = [40, 60, 70, 80, 80]

# the hypothesis talks about the marks obtained by Reeya in different subjects, which is also referenced in the premise
if sum(subjects_hypothesis)!= sum(subjects_premise):
    # check if the total number of subjects in the hypothesis contradicts the total number of subjects in the premise
    label = "contradiction"
else:
    # if the total number of subjects in the hypothesis matches the total number of subjects in the premise, we can infer entailment
    label = "entailment"

print(label)
