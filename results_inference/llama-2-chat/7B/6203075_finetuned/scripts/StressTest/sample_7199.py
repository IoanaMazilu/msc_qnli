points_BC_premise = 3
points_CA_premise = 4
points_AB_premise = 5
points_BC_hypothesis = 7
points_CA_hypothesis = 4
points_AB_hypothesis = 5

# the hypothesis talks about the number of interior points on each side of the triangle, referenced also in the premise
if points_BC_hypothesis!= points_BC_premise:
    # check if the number of points on side BC in the hypothesis contradicts the number of points in the premise
    label = "contradiction"
elif points_CA_hypothesis!= points_CA_premise:
    # check if the number of points on side CA in the hypothesis contradicts the number of points in the premise
    label = "contradiction"
elif points_AB_hypothesis!= points_AB_premise:
    # check if the number of points on side AB in the hypothesis contradicts the number of points in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
