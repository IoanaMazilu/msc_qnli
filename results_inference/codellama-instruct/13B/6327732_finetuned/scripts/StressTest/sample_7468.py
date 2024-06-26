level_premise = 7
level_hypothesis = 1
percentage_premise = 10
percentage_hypothesis = 10

# the hypothesis refers to the number of sales staff with a specific level of education
if level_hypothesis < level_premise:
    # check if the hypothesis value contradicts the estimate of 'level_premise'
    label = "contradiction"
elif percentage_hypothesis!= percentage_premise:
    # check if the percentage of sales staff with a specific level of education in the hypothesis contradicts the percentage mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
