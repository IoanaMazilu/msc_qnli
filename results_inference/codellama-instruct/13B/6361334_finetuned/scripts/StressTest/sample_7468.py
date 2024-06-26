level_premise = 7
level_hypothesis = 1
percentage_premise = 10
percentage_hypothesis = 10

# the hypothesis refers to the level of education required for the sales staff, which is also mentioned in the premise
if level_hypothesis < level_premise:
    # check if the hypothesis value contradicts the level of education required in the premise
    label = "contradiction"
elif percentage_hypothesis!= percentage_premise:
    # check if the percentage of sales staff with level-1 education in the hypothesis contradicts the percentage mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
