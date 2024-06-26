men_premise = 100
km_premise = 2
days_premise = 50
hours_premise = 8
men_hypothesis = 600
km_hypothesis = 2
days_hypothesis = 50
hours_hypothesis = 8

# the hypothesis refers to the number of men, length of the highway, and number of days and hours to build it, as mentioned in the premise
if men_hypothesis <= men_premise:
    # check if the estimate of'men_hypothesis' contradicts the number of men in the premise
    label = "contradiction"
elif km_hypothesis!= km_premise:
    # check if the length of the highway in the hypothesis contradicts the length of the highway reported in the premise
    label = "contradiction"
elif days_hypothesis!= days_premise:
    # check if the number of days to build the highway in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
elif hours_hypothesis!= hours_premise:
    # check if the number of hours to build the highway in the hypothesis contradicts the number of hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
