level_premise = 1
level_hypothesis = 7
percentage_premise = 10
percentage_hypothesis = 10

# the hypothesis refers to the level and percentage of college graduates in Listco's sales staff mentioned in the premise
if level_hypothesis <= level_premise:
    # check if the level in the hypothesis contradicts the level in the premise
    label = "contradiction"
elif percentage_hypothesis!= percentage_premise:
    # check if the percentage in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
