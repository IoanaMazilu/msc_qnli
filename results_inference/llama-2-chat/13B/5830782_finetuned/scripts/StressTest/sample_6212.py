men_premise = 100
men_hypothesis = 200
highway_length_premise = 2
highway_length_hypothesis = 2
days_premise = 50
days_hypothesis = 50
working_hours_premise = 8
working_hours_hypothesis = 8

# the hypothesis refers to the number of men, length of the highway, number of days and working hours
# all these are also mentioned in the premise
if men_premise!= men_hypothesis:
    # check if the number of men in the hypothesis contradicts the number of men reported in the premise
    label = "contradiction"
elif highway_length_premise!= highway_length_hypothesis:
    # check if the length of the highway in the hypothesis contradicts the length of the highway reported in the premise
    label = "contradiction"
elif days_premise!= days_hypothesis:
    # check if the number of days in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
elif working_hours_premise!= working_hours_hypothesis:
    # check if the working hours in the hypothesis contradicts the working hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
