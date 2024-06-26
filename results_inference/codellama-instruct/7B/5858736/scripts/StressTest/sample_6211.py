nhai_men_premise = 600
nhai_men_hypothesis = 100
highway_length_premise = 2
highway_length_hypothesis = 2
days_premise = 50
days_hypothesis = 50
hours_per_day_premise = 8
hours_per_day_hypothesis = 8

# the hypothesis refers to the number of men employed and the length of the highway, mentioned in the premise
if nhai_men_hypothesis <= nhai_men_premise:
    # check if the estimate of 'nhai_men_hypothesis' contradicts the number of men employed in the premise
    label = "contradiction"
elif highway_length_hypothesis!= highway_length_premise:
    # check if the length of the highway in the hypothesis contradicts the length of the highway reported in the premise
    label = "contradiction"
elif days_hypothesis!= days_premise:
    # check if the number of days in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
elif hours_per_day_hypothesis!= hours_per_day_premise:
    # check if the number of hours per day in the hypothesis contradicts the number of hours per day reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
