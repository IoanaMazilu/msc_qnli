premise_points = 500
hypothesis_points = 500

# the premise and hypothesis mention the same number of points for the SENSEX rally
if premise_points!= hypothesis_points:
    # check if the number of points in the hypothesis contradicts the number of points in the premise
    label = "contradiction"
else:
    # the premise and hypothesis mention the same number of points for the SENSEX rally
    # any estimate of the percentage in the hypothesis greater or equal to 'percentage_of_valuation_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
