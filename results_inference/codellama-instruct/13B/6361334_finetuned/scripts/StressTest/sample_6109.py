level_premise = 4
level_hypothesis = 1
percentage_premise = 15
percentage_hypothesis = 15

# the hypothesis refers to the percentage of sales staff with a specific level of education
# the premise mentions a level-less than 4, which is not explicitly mentioned in the hypothesis
if percentage_hypothesis!= percentage_premise:
    # check if the percentage of sales staff with level-1 education in the hypothesis contradicts the percentage mentioned in the premise
    label = "contradiction"
else:
    # the hypothesis does not contradict the premise, but cannot be fully and explicitly entailed from the premise
    label = "neutral"

print(label)
