alice_distance_premise_7am = 300
alice_distance_hypothesis_7am = 100
alice_distance_premise_11am = 100
alice_distance_hypothesis_11am = 100

# the hypothesis refers to the same situation mentioned in the premise
# first we compare the distance between Alice and Bob at 7 am
if alice_distance_premise_7am != alice_distance_hypothesis_7am:
    # if the distance at 7 am in the hypothesis contradicts the one in the premise, we infer contradiction
    label = "contradiction"
# then we compare the distance between Alice and Bob at 11 am
elif alice_distance_premise_11am != alice_distance_hypothesis_11am:
    # if the distance at 11 am in the hypothesis contradicts the one in the premise, we infer contradiction
    label = "contradiction"
else:
    # if the distances in the hypothesis do not contradict the ones in the premise, we infer entailment
    label = "entailment"

print(label)
