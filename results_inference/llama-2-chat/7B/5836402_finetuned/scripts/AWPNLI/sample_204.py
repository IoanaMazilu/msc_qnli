length_premise = 312.0
width_premise = 146.0
area_hypothesis = 45552.0

# the hypothesis refers to the area of the sandbox, which can be calculated from the premise
# compute the area of the sandbox in square centimeters
area_premise = length_premise * width_premise
if area_hypothesis!= area_premise:
    # check if the area in the hypothesis contradicts the area from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
