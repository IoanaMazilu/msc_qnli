# Premise: If Albert’s monthly earnings rise by 14 %, he would earn $678.
# Hypothesis: If Albert’s monthly earnings rise by more than 14 %, he would earn $678.
# Golden Label: contradiction

earnings_rise_premise = 14
earnings_rise_hypothesis = 14
earnings_amount_premise = 678
earnings_amount_hypothesis = 678

# the hypothesis refers to the rise of Albert's earnings and the amount he would earn, both mentioned in the premise
if earnings_rise_hypothesis <= earnings_rise_premise:
    # check if the hypothesis contradicts the premise's assertion of an increase greater than 'earnings_rise_premise'
    label = "contradiction"
elif earnings_amount_hypothesis != earnings_amount_premise:
    # check if the amount Albert would earn according to the hypothesis contradicts the amount mentioned in the premise
    label = "contradiction"
else:
    # the premise gives a specific number for the rise and the amount Albert would earn 
    # any rise greater than 'earnings_rise_premise' and earning amount equal to 'earnings_amount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

