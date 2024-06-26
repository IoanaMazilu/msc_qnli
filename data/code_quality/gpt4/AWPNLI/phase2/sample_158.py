pencil1_premise = 12.0
pencil2_premise = 12.0
total_length_hypothesis = 24.0

# the hypothesis refers to the total length of the pencils, which are also mentioned in the premise
# compute the total length of the pencils in the premise
total_length_premise = pencil1_premise + pencil2_premise
if total_length_hypothesis != total_length_premise:
    # check if the total length of the pencils in the hypothesis contradicts the total length of the pencils from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
