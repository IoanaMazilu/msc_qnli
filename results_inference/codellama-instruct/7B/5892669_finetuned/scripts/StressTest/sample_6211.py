men_premise = 600
men_hypothesis = 100
highway_length_premise = 2
highway_length_hypothesis = 2
work_days_premise = 50
work_days_hypothesis = 50
work_hours_premise = 8
work_hours_hypothesis = 8

# the hypothesis refers to the number of men, the length of the highway, the number of work days and the work hours mentioned in the premise
if men_hypothesis >= men_premise:
    # check if the number of men in the hypothesis contradicts the estimate of less than'men_premise'
    label = "contradiction"
elif highway_length_hypothesis!= highway_length_premise or work_days_hypothesis!= work_days_premise or work_hours_hypothesis!= work_hours_premise:
    # check if the length of the highway, the number of work days or the work hours in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of men
    # any number of men less than'men_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
