# Premise: A restaurant served 7.0 slices of pie during lunch and 5.0 during dinner today and it served 8.0 of them yesterday.
# Hypothesis: 12.0 slices of pie were served today.
# Golden Label: entailment

slices_lunch_premise = 7.0
slices_dinner_premise = 5.0
total_slices_hypothesis = 12.0
slices_yesterday_premise = 8.0

# the hypothesis refers to the total number of slices served today, which are also mentioned in the premise
# compute the total slices served today in the premise
total_slices_premise = slices_lunch_premise + slices_dinner_premise
if total_slices_hypothesis != total_slices_premise:
    # check if the total slices in the hypothesis contradicts the total slices from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
    
print(label)

