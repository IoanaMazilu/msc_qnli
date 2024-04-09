graduates_premise = 10
less_than_7_graduates_hypothesis = 10

# the hypothesis refers to the percentage of sales staff with a certain level of education
if less_than_7_graduates_hypothesis <= graduates_premise:
    # check if the hypothesis value contradicts the estimate of 10% of sales staff with level-1 college education
    label = "contradiction"
elif graduates_premise!= less_than_7_graduates_hypothesis:
    # check if the hypothesis value contradicts the number of sales staff with level-1 college education reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
