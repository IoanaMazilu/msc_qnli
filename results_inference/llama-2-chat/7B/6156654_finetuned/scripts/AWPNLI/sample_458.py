sandcastle_height_miki = 0.8333333333333334
sandcastle_height_sister = 0.5
total_height_sandcastles = sandcastle_height_miki + sandcastle_height_sister

# the hypothesis mentions the total height of both sandcastles, which is also calculated in the premise
if total_height_sandcastles!= 1.33333333333:
    # check if the total height of sandcastles in the hypothesis contradicts the total height of sandcastles in the premise
    label = "contradiction"
else:
    # if the total height of sandcastles in the hypothesis and premise are equal, we can infer entailment
    label = "entailment"

print(label)
