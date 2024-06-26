premise_vikas_rank = 4
premise_tanvi_rank = 8
hypothesis_vikas_rank = 18
hypothesis_tanvi_rank = 21

# the hypothesis refers to the rank of Vikas and Tanvi among the boys and girls in the class
if hypothesis_vikas_rank <= premise_vikas_rank:
    # check if the estimate of 'hypothesis_vikas_rank' contradicts the rank of Vikas in the premise
    label = "contradiction"
elif hypothesis_tanvi_rank!= premise_tanvi_rank:
    # check if the rank of Tanvi in the hypothesis contradicts the rank of Tanvi in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
