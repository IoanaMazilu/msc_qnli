# Premise: Reeya obtained 65, 67, 76, 82 and 85 out of 100 in different subjects, What will be the average.
# Hypothesis: Reeya obtained more than 25, 67, 76, 82 and 85 out of 100 in different subjects, What will be the average.
# Golden Label: entailment

subject1_premise = 65
subject2_premise = 67
subject3_premise = 76
subject4_premise = 82
subject5_premise = 85

subject1_hypothesis = 25
subject2_hypothesis = 67
subject3_hypothesis = 76
subject4_hypothesis = 82
subject5_hypothesis = 85

# the hypothesis refers to the marks obtained by Reeya in different subjects mentioned in the premise
if subject1_hypothesis > subject1_premise:
    # check if the marks obtained in subject1 in the hypothesis contradict the marks obtained in the premise
    label = "contradiction"
elif subject2_hypothesis != subject2_premise or subject3_hypothesis != subject3_premise or subject4_hypothesis != subject4_premise or subject5_hypothesis != subject5_premise:
    # check if the marks obtained in other subjects in the hypothesis contradict the marks obtained in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

