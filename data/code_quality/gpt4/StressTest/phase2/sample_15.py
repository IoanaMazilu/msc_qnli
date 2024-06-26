men_premise = 100
men_hypothesis = 700
highway_length_premise = 2
highway_length_hypothesis = 2
days_premise = 50
days_hypothesis = 50
work_hours_premise = 8
work_hours_hypothesis = 8

# the hypothesis talks about the number of men, length of the highway, number of days and working hours which are all mentioned in the premise
if men_hypothesis < men_premise:
    # check if the hypothesis value contradicts the number of men stated in the premise
    label = "contradiction"
elif highway_length_hypothesis != highway_length_premise or days_hypothesis != days_premise or work_hours_hypothesis != work_hours_premise:
    # check if the length of the highway, number of days or working hours in the hypothesis contradicts the ones reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
