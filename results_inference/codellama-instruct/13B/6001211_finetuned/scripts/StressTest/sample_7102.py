first_distance_premise = 340
first_distance_hypothesis = 240
second_distance_premise = 120
second_distance_hypothesis = 120

# the hypothesis refers to the distances driven at different speeds mentioned in the premise
if first_distance_hypothesis >= first_distance_premise:
    # check if the distance driven at 60 miles per hour in the hypothesis contradicts the estimate of less than 'first_distance_premise'
    label = "contradiction"
elif second_distance_hypothesis!= second_distance_premise:
    # check if the distance driven at 40 miles per hour in the hypothesis contradicts the distance driven at 40 miles per hour in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the first distance driven at 60 miles per hour
    # any distance less than 'first_distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
