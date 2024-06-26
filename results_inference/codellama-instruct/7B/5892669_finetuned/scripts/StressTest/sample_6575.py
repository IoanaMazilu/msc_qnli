vikas_rank_boys_premise = 4
vikas_rank_boys_hypothesis = 4
tanvi_rank_girls_premise = 8
tanvi_rank_girls_hypothesis = 8

# the hypothesis refers to the ranks of Vikas and Tanvi mentioned in the premise
if vikas_rank_boys_hypothesis <= vikas_rank_boys_premise:
    # check if the hypothesis value contradicts the rank of Vikas in the premise
    label = "contradiction"
elif tanvi_rank_girls_hypothesis!= tanvi_rank_girls_premise:
    # check if the rank of Tanvi in the hypothesis contradicts the rank of Tanvi reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
