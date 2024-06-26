employees_premise = 80
employees_hypothesis = 10
graduates_premise = 30
graduates_hypothesis = 30

# the hypothesis talks about the number of level-1 employees and college graduates
# which are also mentioned in the premise
if employees_hypothesis!= employees_premise:
    # check if the number of level-1 employees in the hypothesis contradicts the number in the premise
    label = "contradiction"
elif graduates_hypothesis!= graduates_premise:
    # check if the number of college graduates in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
