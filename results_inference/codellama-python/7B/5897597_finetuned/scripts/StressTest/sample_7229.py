# defining the marks obtained by Nancy in each subject as per the premise
marks_premise = [66, 75, 52, 68, 89]
# defining the marks obtained by Nancy in each subject as per the hypothesis
marks_hypothesis = [86, 75, 52, 68, 89]

# comparing the marks obtained by Nancy in each subject as per the premise and hypothesis
if marks_premise!= marks_hypothesis:
    # if the marks obtained by Nancy in each subject as per the hypothesis contradicts the marks obtained by Nancy in each subject as per the premise
    label = "contradiction"
else:
    # if the marks obtained by Nancy in each subject as per the hypothesis does not contradict the marks obtained by Nancy in each subject as per the premise
    label = "entailment"

print(label)
