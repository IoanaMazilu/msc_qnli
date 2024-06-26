tons_cargo_premise = 8723.0
tons_cargo_unloaded_premise = 5973.0
tons_cargo_hypothesis = 2754.0

# the hypothesis refers to the number of tons of cargo left on the ship, which is also mentioned in the premise
# compute the total number of tons of cargo on the ship
total_tons_cargo_premise = tons_cargo_premise - tons_cargo_unloaded_premise
if total_tons_cargo_premise!= tons_cargo_hypothesis:
    # check if the number of tons of cargo in the hypothesis contradicts the number of tons of cargo from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
