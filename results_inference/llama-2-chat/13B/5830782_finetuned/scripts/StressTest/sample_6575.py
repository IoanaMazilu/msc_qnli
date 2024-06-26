vikas_rank_premise_top = 4
vikas_rank_hypothesis_top = 4
vikas_rank_premise_bottom = 18
vikas_rank_hypothesis_bottom = 18

tanvi_rank_premise_top = 8
tanvi_rank_hypothesis_top = 8
tanvi_rank_premise_bottom = 21
tanvi_rank_hypothesis_bottom = 21

# the hypothesis refers to the ranks of Vikas and Tanvi mentioned in the premise
if vikas_rank_hypothesis_top <= vikas_rank_premise_top or vikas_rank_hypothesis_bottom!= vikas_rank_premise_bottom:
    # check if the hypothesis value contradicts the rank of Vikas in the premise
    label = "contradiction"
elif tanvi_rank_hypothesis_top!= tanvi_rank_premise_top or tanvi_rank_hypothesis_bottom!= tanvi_rank_premise_bottom:
    # check if the rank of Tanvi in the hypothesis contradicts the rank of Tanvi in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
