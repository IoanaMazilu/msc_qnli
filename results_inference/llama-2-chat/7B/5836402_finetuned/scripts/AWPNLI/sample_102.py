boxes_sold_premise = 12.0
cases_needed_hypothesis = 1.0
boxes_hypothesis = 12.0

# the hypothesis refers to the number of boxes and cases needed, which are not mentioned in the premise
# compute the number of boxes needed in the premise
boxes_needed_premise = boxes_sold_premise / cases_needed_hypothesis
if boxes_needed_premise!= boxes_hypothesis:
    # check if the number of boxes needed from the hypothesis contradicts the number of boxes needed from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
