sales_reps_total = 60
hotel_xyz_premise = 0.30 * sales_reps_total
hotel_xyz_hypothesis = 0.10 * sales_reps_total
hotel_abc_premise = 0.70 * sales_reps_total
hotel_abc_hypothesis = 0.70 * sales_reps_total

# the hypothesis refers to the number of sales representatives given accommodation at both hotels, which is mentioned in the premise
if hotel_xyz_premise <= hotel_xyz_hypothesis:
    # check if the estimate of 'hotel_xyz_hypothesis' contradicts the number of sales representatives at Hotel XYZ in the premise
    label = "contradiction"
elif hotel_abc_hypothesis != hotel_abc_premise:
    # check if the number of sales representatives at Hotel ABC in the hypothesis contradicts the number of sales representatives at Hotel ABC reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
