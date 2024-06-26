scientific_name:employment_premise
employment_premise_level_1_employees_premise:80
employment_premise_college_graduates_premise:30
employment_hypothesis_level_1_employees_hypothesis:60
employment_hypothesis_college_graduates_hypothesis:30

# the hypothesis refers to the number of level-1 employees and college graduates at Amtek, which are also mentioned in the premise
if employment_hypothesis_level_1_employees_hypothesis <= employment_premise_level_1_employees_premise:
    # check if the number of level-1 employees in the hypothesis contradicts the number of level-1 employees in the premise
    label = "contradiction"
elif employment_hypothesis_college_graduates_hypothesis!= employment_premise_college_graduates_premise:
    # check if the number of college graduates in the hypothesis contradicts the number of college graduates in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
