employees_premise = 180
employees_hypothesis = 280

# the hypothesis refers to the number of employees at Veridux Corporation
if employees_hypothesis <= employees_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif employees_premise!= employees_hypothesis:
    # check if the number of employees in the hypothesis contradicts the number of employees reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimate do not contradict the premise, we can infer neutrality
    label = "neutral"

print(label)
