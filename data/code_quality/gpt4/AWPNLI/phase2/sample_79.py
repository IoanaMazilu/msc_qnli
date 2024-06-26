slices_lunch_premise = 7.0
slices_dinner_premise = 5.0
slices_today_hypothesis = 11.0

# the hypothesis refers to the number of slices served today, which is also mentioned in the premise
# compute the total number of slices served today in the premise
total_slices_today_premise = slices_lunch_premise + slices_dinner_premise
if slices_today_hypothesis != total_slices_today_premise:
    # check if the number of slices served today in the hypothesis contradicts the number from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
