men_premise = 600
men_hypothesis = 100
highway_length_premise = 2
highway_length_hypothesis = 2
days_premise = 50
days_hypothesis = 50
hours_premise = 8
hours_hypothesis = 8

# the hypothesis refers to the number of men, length of the highway, days to complete it and hours worked per day mentioned in the premise
if men_hypothesis <= men_premise:
    # check if the estimate of'men_hypothesis' contradicts the number of men in the premise
    label = "contradiction"
elif highway_length_hypothesis!= highway_length_premise:
    # check if the length of the highway in the hypothesis contradicts the length of the highway reported in the premise
    label = "contradiction"
elif days_hypothesis!= days_premise:
    # check if the number of days to complete the highway in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
elif hours_hypothesis!= hours_premise:
    # check if the number of hours worked per day in the hypothesis contradicts the number of hours worked per day reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
