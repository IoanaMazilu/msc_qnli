men_premise = 100
men_hypothesis = 200
days_premise = 50
days_hypothesis = 50
hours_premise = 8
hours_hypothesis = 8

# the hypothesis refers to the number of men and days working on the highway, as mentioned in the premise
if men_hypothesis <= men_premise:
    # check if the estimate of'men_hypothesis' contradicts the number of men in the premise
    label = "contradiction"
elif days_hypothesis!= days_premise:
    # check if the number of days in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
