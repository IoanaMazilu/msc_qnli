rajat_questions_premise = 7
vikas_questions_premise = 3
abhishek_questions_premise = 2

rajat_questions_hypothesis = 8
vikas_questions_hypothesis = 3
abhishek_questions_hypothesis = 2

# the hypothesis refers to the ratio of questions submitted by Rajat, Vikas and Abhishek mentioned in the premise
if rajat_questions_premise >= rajat_questions_hypothesis:
    # check if the estimate of 'rajat_questions_hypothesis' contradicts the number of Rajat's questions in the premise
    label = "contradiction"
elif vikas_questions_hypothesis!= vikas_questions_premise or abhishek_questions_hypothesis!= abhishek_questions_premise:
    # check if the number of Vikas's or Abhishek's questions in the hypothesis contradicts the number of questions reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
