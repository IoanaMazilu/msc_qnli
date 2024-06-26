average_score_premise = sum(x for x in range(100))
average_score_hypothesis = sum(x for x in range(100))

# the hypothesis refers to the scores Reeya obtained in different subjects
if average_score_premise >= average_score_hypothesis:
    # check if the average score in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # if the average score in the premise is less than the average score in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
