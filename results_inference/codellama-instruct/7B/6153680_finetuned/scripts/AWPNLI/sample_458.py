miki_sandcastle_height = 0.8333333333333334
sister_sandcastle_height = 0.5
total_height = 1.33333333333

# the hypothesis refers to the total height of both sandcastles, which is also mentioned in the premise
if total_height!= (miki_sandcastle_height + sister_sandcastle_height):
    # check if the total height in the hypothesis contradicts the total height mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and the premise values match, we can infer entailment
    label = "entailment"

print(label)
