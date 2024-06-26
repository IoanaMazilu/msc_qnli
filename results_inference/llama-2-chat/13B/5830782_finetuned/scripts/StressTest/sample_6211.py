men_premise = 600
men_hypothesis = 100
highway_length_premise = 2
highway_length_hypothesis = 2
days_premise = 50
days_hypothesis = 50
working_hours_premise = 8
working_hours_hypothesis = 8

# the hypothesis talks about the number of men, length of highway, number of days and working hours, all mentioned in the premise
if men_hypothesis >= men_premise:
    # check if the number of men in the hypothesis contradicts the estimate of less than'men_premise'
    label = "contradiction"
elif highway_length_hypothesis!= highway_length_premise or days_hypothesis!= days_premise or working_hours_hypothesis!= working_hours_premise:
    # check if the length of the highway, number of days or working hours in the hypothesis contradict the ones reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of men
    # any number of men less than'men_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
