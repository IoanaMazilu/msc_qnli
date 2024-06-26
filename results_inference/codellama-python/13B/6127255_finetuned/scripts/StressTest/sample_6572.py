rank_vikas_premise = 9
rank_vikas_hypothesis = 9
rank_tanvi_premise = 17
rank_tanvi_hypothesis = 17

# the hypothesis refers to the ranks of Vikas and Tanvi mentioned in the premise
if rank_vikas_hypothesis <= rank_vikas_premise:
    # check if the hypothesis value contradicts the rank of Vikas in the premise
    label = "contradiction"
elif rank_tanvi_hypothesis!= rank_tanvi_premise:
    # check if the rank of Tanvi in the hypothesis contradicts the rank of Tanvi in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
