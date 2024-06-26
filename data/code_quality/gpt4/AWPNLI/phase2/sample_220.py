doughnuts_premise = 48.0
boxes_premise = 4.0
doughnuts_per_box_hypothesis = 12.0

# the hypothesis refers to the number of doughnuts per box, which is also implicitly mentioned in the premise
# compute the number of doughnuts per box in the premise
doughnuts_per_box_premise = doughnuts_premise / boxes_premise
if doughnuts_per_box_hypothesis != doughnuts_per_box_premise:
    # check if the number of doughnuts per box in the hypothesis contradicts the number of doughnuts per box from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
