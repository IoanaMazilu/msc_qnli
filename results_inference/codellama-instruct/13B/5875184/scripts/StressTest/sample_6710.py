premise_points = 60
hypothesis_points = 60
premise_percentage = 60
hypothesis_percentage = 60

# the hypothesis talks about the number of points scored by the team and the percentage of points accounted for by Jason
if hypothesis_points < premise_points:
    # check if the hypothesis value contradicts the number of points scored in the premise
    label = "contradiction"
elif hypothesis_percentage!= premise_percentage:
    # check if the hypothesis value contradicts the percentage of points accounted for by Jason in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of points scored and the percentage of points accounted for by Jason
    # any number of points greater than 'premise_points' and any percentage of points accounted for by Jason greater than 'premise_percentage' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
