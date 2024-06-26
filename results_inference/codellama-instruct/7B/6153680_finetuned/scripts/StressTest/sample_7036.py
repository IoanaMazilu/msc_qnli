speed_fred = 8
speed_sam = 5

# the hypothesis refers to the speed of Fred and Sam
# the premise gives the speed of Fred and Sam
if speed_fred!= 5:
    # check if the speed of Fred in the hypothesis contradicts the speed of Fred in the premise
    label = "contradiction"
elif speed_sam!= 5:
    # check if the speed of Sam in the hypothesis contradicts the speed of Sam in the premise
    label = "contradiction"
else:
    # if the hypothesis values and premise values match, we can infer entailment
    label = "entailment"

print(label)
