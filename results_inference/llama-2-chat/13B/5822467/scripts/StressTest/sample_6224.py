mani_share_premise = 200
rani_share_premise = 200
mani_share_hypothesis = 250
rani_share_hypothesis = 300

# the hypothesis refers to the difference between Mani and Rani's share
if mani_share_hypothesis <= mani_share_premise:
    # check if the estimate of'mani_share_hypothesis' contradicts the premise
    label = "contradiction"
elif rani_share_hypothesis!= rani_share_premise:
    # check if the number of shares for Rani in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
