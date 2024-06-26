premise_points = 500
hypothesis_points = 0

# the premise mentions a rally of 500 points in the SENSEX
# the hypothesis mentions a downward trend in the Sensex and Nifty
if premise_points < hypothesis_points:
    # check if the number of points in the hypothesis contradicts the number of points in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of points
    # any estimate of the number of points in the hypothesis greater or equal to 'premise_points' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
