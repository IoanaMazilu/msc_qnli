# Premise: Reeya obtained more than 45, 67, 76, 82 and 85 out of 100 in different subjects, What will be the average.
# Hypothesis: Reeya obtained 55, 67, 76, 82 and 85 out of 100 in different subjects, What will be the average.
# Golden Label: neutral

# defining variables for the marks obtained in different subjects in the premise and hypothesis
marks_premise = [45, 67, 76, 82, 85]
marks_hypothesis = [55, 67, 76, 82, 85]

# the hypothesis talks about the marks obtained by Reeya in different subjects, which is also referenced in the premise
# first, we will check if the marks obtained in the hypothesis contradict the estimate of more than 45 in the premise
for i in range(len(marks_premise)):
    if marks_hypothesis[i] <= marks_premise[i]:
        label = "contradiction"
        break
else:
    # if the hypothesis does not contradict the premise, we will check if it can be explicitly entailed from the premise
    if marks_hypothesis == marks_premise:
        label = "entailment"
    else:
        # any marks obtained greater than 45 is consistent with the premise, but cannot be explicitly entailed from the premise
        label = "neutral"

print(label)

