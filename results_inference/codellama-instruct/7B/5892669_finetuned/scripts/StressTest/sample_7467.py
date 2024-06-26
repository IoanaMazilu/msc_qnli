level_graduates_premise = 10
level_graduates_hypothesis = 7
percentage_premise = 10
percentage_hypothesis = 10

# the hypothesis refers to the percentage of Level-less than 'level_graduates_hypothesis' college graduates in Listco's sales staff
if percentage_hypothesis!= percentage_premise:
    # check if the percentage in the hypothesis contradicts the percentage mentioned in the premise
    label = "contradiction"
elif level_graduates_hypothesis <= level_graduates_premise:
    # check if the level of graduates in the hypothesis contradicts the level of graduates mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
