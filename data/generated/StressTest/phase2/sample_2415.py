# Premise: Reeya obtained 50, 60, 70, 80 and 80 out of 100 in different subjects, What will be the average.
# Hypothesis: Reeya obtained more than 20, 60, 70, 80 and 80 out of 100 in different subjects, What will be the average.
# Golden Label: entailment

subject1_premise = 50
subject2_premise = 60
subject3_premise = 70
subject4_premise = 80
subject5_premise = 80

subject1_hypothesis = 20
subject2_hypothesis = 60
subject3_hypothesis = 70
subject4_hypothesis = 80
subject5_hypothesis = 80

# the hypothesis refers to the marks obtained by Reeya in different subjects as mentioned in the premise
if subject1_hypothesis >= subject1_premise:
    # check if the mark of 'subject1_hypothesis' contradicts the score of subject1 in the premise
    label = "contradiction"
elif subject2_hypothesis != subject2_premise or subject3_hypothesis != subject3_premise or subject4_hypothesis != subject4_premise or subject5_hypothesis != subject5_premise:
    # check if the marks of any other subjects in the hypothesis contradict the scores reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

