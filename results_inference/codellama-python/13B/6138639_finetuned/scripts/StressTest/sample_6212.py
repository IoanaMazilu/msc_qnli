men_premise = 100
men_hypothesis = 200
highway_length_premise = 2
highway_length_hypothesis = 2
working_hours_premise = 8
working_hours_hypothesis = 8
days_premise = 50
days_hypothesis = 50

# the hypothesis refers to the number of men employed by NHAI, the length of the highway and the working hours, all mentioned in the premise
if men_hypothesis!= men_premise:
    # check if the number of men in the hypothesis contradicts the number of men reported in the premise
    label = "contradiction"
elif highway_length_hypothesis!= highway_length_premise or working_hours_hypothesis!= working_hours_premise or days_hypothesis!= days_premise:
    # check if the length of the highway or the working hours in the hypothesis contradicts the ones reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
