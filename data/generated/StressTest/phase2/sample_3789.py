# Premise: Jill has 21 gallons of water stored in quart, half-gallon, and one gallon jars.
# Hypothesis: Jill has less than 51 gallons of water stored in quart, half-gallon, and one gallon jars.
# Golden Label: entailment

water_gallons_premise = 21
water_gallons_hypothesis = 51

# the hypothesis refers to the amount of water in gallons stored by Jill, which is also mentioned in the premise
if water_gallons_hypothesis <= water_gallons_premise:
    # check if the hypothesis value contradicts the exact amount of water 'water_gallons_premise'
    label = "contradiction"
elif water_gallons_premise > water_gallons_hypothesis:
    # check if the exact number of gallons in the premise contradicts the estimate of less than 'water_gallons_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

