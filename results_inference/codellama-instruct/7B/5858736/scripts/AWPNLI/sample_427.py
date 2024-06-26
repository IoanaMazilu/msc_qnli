cargo_ship_premise = 8723.0
cargo_bahamas_premise = 5973.0
cargo_hypothesis = 2754.0

# the hypothesis refers to the number of tons of cargo left on the ship
# compute the total number of tons of cargo left on the ship
cargo_left_premise = cargo_ship_premise - cargo_bahamas_premise
if cargo_left_premise!= cargo_hypothesis:
    # check if the number of tons of cargo left on the ship contradicts the estimate of 2754.0 tons
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
