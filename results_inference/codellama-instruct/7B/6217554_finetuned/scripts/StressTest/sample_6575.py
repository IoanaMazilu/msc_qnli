vikas_boy_rank_premise = 4
vikas_boy_rank_hypothesis = 4
vikas_girl_rank_premise = 18
vikas_girl_rank_hypothesis = 18
tanvi_boy_rank_premise = 8
tanvi_boy_rank_hypothesis = 8
tanvi_girl_rank_premise = 21
tanvi_girl_rank_hypothesis = 21

# the hypothesis refers to the ranks of Vikas and Tanvi mentioned in the premise
if vikas_boy_rank_hypothesis <= vikas_boy_rank_premise:
    # check if the estimate of 'vikas_boy_rank_hypothesis' contradicts the rank of Vikas reported in the premise
    label = "contradiction"
elif vikas_girl_rank_hypothesis!= vikas_girl_rank_premise:
    # check if the rank of Tanvi in the hypothesis contradicts the rank of Tanvi reported in the premise
    label = "contradiction"
elif tanvi_boy_rank_hypothesis!= tanvi_boy_rank_premise:
    # check if the rank of Tanvi in the hypothesis contradicts the rank of Tanvi reported in the premise
    label = "contradiction"
elif tanvi_girl_rank_hypothesis!= tanvi_girl_rank_premise:
    # check if the rank of Tanvi in the hypothesis contradicts the rank of Tanvi reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
