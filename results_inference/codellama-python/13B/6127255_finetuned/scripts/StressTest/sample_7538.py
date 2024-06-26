subject1_premise = 40
subject2_premise = 60
subject3_premise = 70
subject4_premise = 80
subject5_premise = 80

subject1_hypothesis = 40
subject2_hypothesis = 60
subject3_hypothesis = 70
subject4_hypothesis = 80
subject5_hypothesis = 80

# the hypothesis refers to the marks obtained by Reeya in different subjects mentioned in the premise
if subject1_hypothesis >= subject1_premise or subject2_hypothesis >= subject2_premise or subject3_hypothesis >= subject3_premise or subject4_hypothesis >= subject4_premise or subject5_hypothesis >= subject5_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
