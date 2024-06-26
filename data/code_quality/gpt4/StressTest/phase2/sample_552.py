subject1_premise = 65
subject2_premise = 67
subject3_premise = 76
subject4_premise = 82
subject5_premise = 85

subject1_hypothesis = 45
subject2_hypothesis = 67
subject3_hypothesis = 76
subject4_hypothesis = 82
subject5_hypothesis = 85

# the hypothesis refers to the number of marks obtained by Reeya in different subjects, mentioned in the premise
if subject1_premise <= subject1_hypothesis:
    # check if the hypothesis value contradicts the number of marks obtained in subject1 in the premise
    label = "contradiction"
elif subject2_premise != subject2_hypothesis or subject3_premise != subject3_hypothesis or subject4_premise != subject4_hypothesis or subject5_premise != subject5_hypothesis:
    # check if the number of marks obtained in any of the other subjects contradicts the number of marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
