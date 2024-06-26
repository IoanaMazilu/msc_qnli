space_debris_premise = 6000
space_debris_hypothesis = 6000

# the hypothesis mentions the quantity of space debris in orbit, which is also mentioned in the premise
if space_debris_hypothesis != space_debris_premise:
    # check if the quantity of space debris in the hypothesis contradicts the quantity stated in the premise
    label = "contradiction"
else:
    # if the hypothesis' quantity of space debris does not contradict the premise's quantity, we can infer entailment
    label = "entailment"

print(label)
