pieces_clothing_premise = 47.0
pieces_clothing_hypothesis = 10.0
loads_premise = 5.0
loads_hypothesis = 1.0

# the hypothesis refers to the number of pieces of clothing that can go in each load, which is also mentioned in the premise
# compute the total number of pieces of clothing in the premise
total_pieces_clothing_premise = pieces_clothing_premise / loads_premise
if total_pieces_clothing_premise!= pieces_clothing_hypothesis:
    # check if the number of pieces of clothing in the hypothesis contradicts the number of pieces of clothing from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
