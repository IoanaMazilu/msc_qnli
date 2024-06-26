men_premise = 100
men_hypothesis = 600
highway_length_premise = 2
highway_length_hypothesis = 2
days_premise = 50
days_hypothesis = 50
hours_premise = 8
hours_hypothesis = 8

# the hypothesis refers to the number of men, the length of the highway, the number of days and the working hours mentioned in the premise
if men_premise >= men_hypothesis:
    # check if the estimate of'men_hypothesis' contradicts the number of men in the premise
    label = "contradiction"
elif highway_length_premise!= highway_length_hypothesis or days_premise!= days_hypothesis or hours_premise!= hours_hypothesis:
    # check if the length of the highway, the number of days or the working hours in the hypothesis contradicts the values reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
