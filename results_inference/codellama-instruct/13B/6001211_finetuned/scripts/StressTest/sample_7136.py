st_tv_premise = 10
st_tv_hypothesis = 70
sv_premise = 12
sv_hypothesis = 12

# the hypothesis refers to the sides of the same triangle mentioned in the premise
if st_tv_hypothesis!= st_tv_premise:
    # check if the length of sides ST and TV in the hypothesis contradicts the length of sides ST and TV reported in the premise
    label = "contradiction"
elif sv_hypothesis!= sv_premise:
    # check if the length of side SV in the hypothesis contradicts the length of side SV reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
