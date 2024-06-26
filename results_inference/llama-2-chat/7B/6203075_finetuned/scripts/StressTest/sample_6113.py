employees_premise = 80
employees_hypothesis = 10
graduates_premise = 30
graduates_hypothesis = 30

# the hypothesis refers to the number of level-1 employees and college graduates at Amtek
if employees_premise!= employees_hypothesis:
    # check if the number of level-1 employees in the hypothesis contradicts the number in the premise
    label = "contradiction"
elif graduates_hypothesis!= graduates_premise:
    # check if the number of college graduates in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
