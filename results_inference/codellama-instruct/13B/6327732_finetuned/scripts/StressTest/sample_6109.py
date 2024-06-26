level_premise = 4
level_hypothesis = 1
percentage_premise = 15
percentage_hypothesis = 15

# the hypothesis refers to the percentage of sales staff with a specific level of education
if percentage_hypothesis!= percentage_premise:
    # check if the percentage of sales staff with a level-1 college graduate in the hypothesis contradicts the percentage mentioned in the premise
    label = "contradiction"
elif level_hypothesis < level_premise:
    # check if the level of education in the hypothesis is less than the level mentioned in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
