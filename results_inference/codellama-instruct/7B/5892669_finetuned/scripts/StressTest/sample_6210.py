men_premise = 100
men_hypothesis = 600
highway_length_premise = 2
highway_length_hypothesis = 2
work_days_premise = 50
work_days_hypothesis = 50
work_hours_premise = 8
work_hours_hypothesis = 8

# the hypothesis refers to the number of men, the length of the highway, the number of work days and the work hours mentioned in the premise
if men_hypothesis <= men_premise:
    # check if the estimate of'men_hypothesis' contradicts the number of men in the premise
    label = "contradiction"
elif highway_length_hypothesis!= highway_length_premise or work_days_hypothesis!= work_days_premise or work_hours_hypothesis!= work_hours_premise:
    # check if the length of the highway, the number of work days or the work hours in the hypothesis contradicts the corresponding values in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
