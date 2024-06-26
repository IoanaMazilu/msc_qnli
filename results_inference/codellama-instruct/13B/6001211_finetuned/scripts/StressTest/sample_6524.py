subject1_premise = 55
subject2_premise = 67
subject3_premise = 76
subject4_premise = 82
subject5_premise = 85

subject1_hypothesis = 35
subject2_hypothesis = 67
subject3_hypothesis = 76
subject4_hypothesis = 82
subject5_hypothesis = 85

# the hypothesis refers to the marks obtained by Reeya in different subjects, mentioned also in the premise
if subject1_premise!= subject1_hypothesis:
    # check if the mark obtained in the first subject in the hypothesis contradicts the mark obtained in the first subject in the premise
    label = "contradiction"
elif subject2_premise!= subject2_hypothesis or subject3_premise!= subject3_hypothesis or subject4_premise!= subject4_hypothesis or subject5_premise!= subject5_hypothesis:
    # check if the marks obtained in the second, third, fourth or fifth subjects in the hypothesis contradict the marks obtained in the same subjects in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
