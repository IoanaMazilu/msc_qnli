mani_share_premise = 200
rani_share_premise = 200
mani_share_hypothesis = 400
rani_share_hypothesis = 400

# the hypothesis refers to the difference between Mani and Rani's share
if mani_share_hypothesis <= mani_share_premise:
    # check if the estimate of'mani_share_hypothesis' contradicts the difference between Mani and Rani's share in the premise
    label = "contradiction"
elif rani_share_hypothesis!= rani_share_premise:
    # check if the difference between Rani and Mani's share in the hypothesis contradicts the difference between Rani and Mani's share reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
