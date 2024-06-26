men_premise = 100
men_hypothesis = 200
highway_length_premise = 2
highway_length_hypothesis = 2
days_premise = 50
days_hypothesis = 50
working_hours_premise = 8
working_hours_hypothesis = 8

# the hypothesis refers to the number of men, the length of the highway, the number of days and the working hours per day
if highway_length_hypothesis!= highway_length_premise or days_hypothesis!= days_premise or working_hours_hypothesis!= working_hours_premise:
    # check if the length of the highway, the number of days or the working hours per day in the hypothesis contradicts the premise
    label = "contradiction"
elif men_hypothesis!= men_premise:
    # check if the number of men in the hypothesis contradicts the number of men in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
