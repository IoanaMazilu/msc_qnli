men_premise = 100
men_hypothesis = 600
distance_premise = 2
distance_hypothesis = 2
working_hours_premise = 8
working_hours_hypothesis = 8
days_premise = 50
days_hypothesis = 50

# the hypothesis talks about the number of men employed to build a highway,
# which is also mentioned in the premise
if men_hypothesis <= men_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif distance_hypothesis!= distance_premise:
    # check if the distance in the hypothesis contradicts the distance in the premise
    label = "contradiction"
elif working_hours_hypothesis!= working_hours_premise:
    # check if the working hours in the hypothesis contradicts the working hours in the premise
    label = "contradiction"
elif days_hypothesis!= days_premise:
    # check if the number of days in the hypothesis contradicts the number of days in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
