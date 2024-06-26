ratio_questions_premise = (7, 3, 2)
ratio_questions_hypothesis = (8, 3, 2)

# the hypothesis refers to the ratio of questions submitted by Rajat, Vikas and Abhishek mentioned in the premise
if ratio_questions_premise <= ratio_questions_hypothesis:
    # check if the estimate of 'ratio_questions_hypothesis' contradicts the ratio of questions submitted in the premise
    label = "contradiction"
elif ratio_questions_hypothesis!= ratio_questions_premise:
    # check if the ratio of questions in the hypothesis contradicts the ratio of questions reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
