rank_of_vikas_premise = 7
rank_of_vikas_hypothesis = 9
rank_of_tanvi_premise = 17
rank_of_tanvi_hypothesis = 17

# the hypothesis talks about the rank of Vikas and Tanvi, which are also mentioned in the premise
if rank_of_vikas_hypothesis <= rank_of_vikas_premise:
    # check if the rank of Vikas in the hypothesis contradicts the premise
    label = "contradiction"
elif rank_of_tanvi_hypothesis!= rank_of_tanvi_premise:
    # check if the rank of Tanvi in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the rank of Vikas and Tanvi in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
