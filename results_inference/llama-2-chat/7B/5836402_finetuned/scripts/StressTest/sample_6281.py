rajat_questions_premise = 7
vikas_questions_premise = 3
abhishek_questions_premise = 2

rajat_questions_hypothesis = 5
vikas_questions_hypothesis = 3
abhishek_questions_hypothesis = 2

# the hypothesis refers to the ratio of questions submitted by each person mentioned in the premise
if rajat_questions_premise!= rajat_questions_hypothesis or vikas_questions_premise!= vikas_questions_hypothesis or abhishek_questions_premise!= abhishek_questions_hypothesis:
    # check if the ratio of questions in the hypothesis contradicts the ratio of questions in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
