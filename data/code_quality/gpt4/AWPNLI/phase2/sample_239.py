total_pages_premise = 120.0
pages_night_hypothesis = 9.0
total_days_hypothesis = 10.0

# the hypothesis refers to the number of pages to read each night and the total days, which can be calculated from the premise
# compute the number of pages to read each night in the premise
pages_night_premise = total_pages_premise / total_days_hypothesis
if pages_night_hypothesis != pages_night_premise:
    # check if the number of pages to read each night in the hypothesis contradicts the computed value from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
