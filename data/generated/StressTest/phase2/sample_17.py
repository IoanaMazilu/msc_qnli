# Premise: NHAI employs 100 men to build a highway of 2 km in 50 days working 8 hours a day.
# Hypothesis: NHAI employs 400 men to build a highway of 2 km in 50 days working 8 hours a day.
# Golden Label: contradiction

men_premise = 100
men_hypothesis = 400
highway_length_premise = 2
highway_length_hypothesis = 2
days_premise = 50
days_hypothesis = 50
working_hours_premise = 8
working_hours_hypothesis = 8

# the hypothesis refers to the number of men employed by NHAI, 
# the length of the highway, the number of days and the working hours per day, all mentioned in the premise
if highway_length_hypothesis != highway_length_premise or days_hypothesis != days_premise or working_hours_hypothesis != working_hours_premise:
    # check if the length of the highway, the number of days or the working hours per day in the hypothesis contradict the ones in the premise
    label = "contradiction"
elif men_hypothesis != men_premise:
    # check if the number of men in the hypothesis contradicts the number of men in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

