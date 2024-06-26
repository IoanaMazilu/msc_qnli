salary_saved_premise = 10
salary_saved_hypothesis = 70

# the hypothesis talks about the percentage of the monthly salary saved by Kishore, which is also referenced in the premise
if salary_saved_premise >= salary_saved_hypothesis:
    # check if the percentage of salary saved in the premise contradicts the hypothesis estimate of less than 'salary_saved_hypothesis'
    label = "contradiction"
else:
    # if the premise value does not contradict the estimate in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
