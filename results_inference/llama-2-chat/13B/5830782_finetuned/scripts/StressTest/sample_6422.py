# defining the marks obtained by Arun in different subjects according to the premise and hypothesis
marks_premise = [76, 65, 82, 67, 85]
marks_hypothesis = [46, 65, 82, 67, 85]

# checking if the marks obtained in the hypothesis contradict the marks obtained in the premise
if marks_premise!= marks_hypothesis:
    label = "contradiction"
else:
    # if the marks obtained in the hypothesis do not contradict the marks obtained in the premise, we can infer entailment
    label = "entailment"

print(label)
