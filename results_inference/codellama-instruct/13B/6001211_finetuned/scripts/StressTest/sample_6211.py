men_premise = 600
men_hypothesis = 100
highway_length_premise = 2
highway_length_hypothesis = 2
days_premise = 50
days_hypothesis = 50
work_hours_premise = 8
work_hours_hypothesis = 8

# the hypothesis refers to the number of men employed by NHAI, the length of the highway, the number of days and the working hours per day, all mentioned in the premise
if highway_length_hypothesis!= highway_length_premise:
    # check if the length of the highway in the hypothesis contradicts the length of the highway in the premise
    label = "contradiction"
elif days_hypothesis!= days_premise:
    # check if the number of days in the hypothesis contradicts the number of days in the premise
    label = "contradiction"
elif work_hours_hypothesis!= work_hours_premise:
    # check if the working hours per day in the hypothesis contradicts the working hours per day in the premise
    label = "contradiction"
elif men_hypothesis >= men_premise:
    # check if the number of men in the hypothesis contradicts the estimate of less than'men_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of men
    # any number of men less than'men_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
