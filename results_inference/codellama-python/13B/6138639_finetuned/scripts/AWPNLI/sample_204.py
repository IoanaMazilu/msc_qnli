length_premise = 312.0
width_premise = 146.0
area_hypothesis = 45552.0

# the hypothesis refers to the area of the sandbox, which is also mentioned in the premise
# compute the area of the sandbox in the premise
area_premise = length_premise * width_premise
if area_hypothesis!= area_premise:
    # check if the area of the sandbox in the hypothesis contradicts the area of the sandbox from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
