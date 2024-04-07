# Premise: Mary needs some meat from the butchers shop a meter away from her house. Each step Mary takes is less than 60 centimeters. How many minutes will it take if each step lasts a minute?
# Hypothesis: Mary needs some meat from the butchers shop a meter away from her house. Each step Mary takes is 20 centimeters. How many minutes will it take if each step lasts a minute?
# Golden Label: neutral

step_distance_premise = 60
step_distance_hypothesis = 20

# the hypothesis refers to the length of Mary's steps mentioned in the premise
if step_distance_hypothesis > step_distance_premise:
    # check if the length of Mary's steps in the hypothesis contradicts the maximum length of Mary's steps reported in the premise
    label = "contradiction"
elif step_distance_hypothesis < step_distance_premise:
    # check if the length of Mary's steps in the hypothesis is less than the maximum length of Mary's steps reported in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

