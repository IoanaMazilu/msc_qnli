subject1_premise = 50
subject2_premise = 60
subject3_premise = 70
subject4_premise = 80
subject5_premise = 80

subject1_hypothesis = 40
subject2_hypothesis = 60
subject3_hypothesis = 70
subject4_hypothesis = 80
subject5_hypothesis = 80

# the hypothesis talks about the marks obtained by Reeya in different subjects, referenced also in the premise
if subject1_hypothesis >= subject1_premise:
    # check if the hypothesis value contradicts the estimate of less than'subject1_premise'
    label = "contradiction"
elif subject2_hypothesis!= subject2_premise or subject3_hypothesis!= subject3_premise or subject4_hypothesis!= subject4_premise or subject5_hypothesis!= subject5_premise:
    # check if the marks in other subjects in the hypothesis contradict the marks in the same subjects reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the marks in subject1
    # any marks less than'subject1_premise' in subject1 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
