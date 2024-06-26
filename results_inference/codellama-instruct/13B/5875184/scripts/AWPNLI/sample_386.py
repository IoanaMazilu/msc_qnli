premise_keith_picked = 47.0
premise_mike_picked = 12.0
premise_keith_gave_away = 46.0
hypothesis_mike_has = 13.0

# the hypothesis refers to the number of pears left, which are also mentioned in the premise
# compute the total number of pears picked by both Keith and Mike
total_picked = premise_keith_picked + premise_mike_picked

# check if the number of pears given away by Keith contradicts the total number of pears picked
if premise_keith_gave_away > total_picked:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
