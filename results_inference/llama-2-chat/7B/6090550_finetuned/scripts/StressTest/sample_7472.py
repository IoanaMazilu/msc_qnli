ys_premise_employees_level1 = 72
ys_hypothesis_employees_level1 = 62
ys_premise_graduates_level1 = 30
ys_hypothesis_graduates_level1 = 30

# the hypothesis talks about the number of level-1 employees and graduates, which are also mentioned in the premise
if ys_hypothesis_employees_level1!= ys_premise_employees_level1:
    # check if the number of level-1 employees in the hypothesis contradicts the number of level-1 employees in the premise
    label = "contradiction"
elif ys_hypothesis_graduates_level1!= ys_premise_graduates_level1:
    # check if the number of graduates in the hypothesis contradicts the number of graduates in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

