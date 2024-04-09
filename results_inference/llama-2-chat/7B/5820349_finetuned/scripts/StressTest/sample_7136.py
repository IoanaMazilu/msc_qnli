st_tv_side_premise = 10
st_tv_side_hypothesis = 70
sv_side_premise = 12
sv_side_hypothesis = 12

# the hypothesis refers to the sides of the triangle STV mentioned in the premise
if st_tv_side_premise!= st_tv_side_hypothesis:
    # check if the sides of the triangle STV in the hypothesis contradicts the sides reported in the premise
    label = "contradiction"
elif sv_side_hypothesis!= sv_side_premise:
    # check if the side of the SV in the hypothesis contradicts the side reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
