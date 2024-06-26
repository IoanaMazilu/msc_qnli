men_premise = 600
men_hypothesis = 100
highway_length_premise = 2
highway_length_hypothesis = 2
working_days_premise = 50
working_days_hypothesis = 50
working_hours_premise = 8
working_hours_hypothesis = 8

# the hypothesis refers to the number of men employed, the length of the highway, 
# the number of working days and hours mentioned in the premise
if men_hypothesis >= men_premise:
    # check if the number of men in the hypothesis contradicts the estimate of less than 'men_premise'
    label = "contradiction"
elif highway_length_hypothesis != highway_length_premise or working_days_hypothesis != working_days_premise or working_hours_hypothesis != working_hours_premise:
    # check if the length of the highway, the number of working days or hours in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
