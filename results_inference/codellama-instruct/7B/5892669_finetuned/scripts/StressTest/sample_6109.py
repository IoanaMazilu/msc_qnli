level_premise = 4
level_hypothesis = 1
percentage_premise = 15
percentage_hypothesis = 15

# the hypothesis refers to the level of college graduates and their percentage in Amtek's sales staff, mentioned in the premise
if level_hypothesis >= level_premise:
    # check if the level of 'level_hypothesis' contradicts the level of college graduates in the premise
    label = "contradiction"
elif percentage_hypothesis!= percentage_premise:
    # check if the percentage of college graduates in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
