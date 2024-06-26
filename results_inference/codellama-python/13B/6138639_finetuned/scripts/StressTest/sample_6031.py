# define the variables for the premise and hypothesis
distance_traveled_premise = 8/2
distance_traveled_hypothesis = 1/2

# the hypothesis refers to the distance traveled by Maria, which is also mentioned in the premise
if distance_traveled_hypothesis > distance_traveled_premise:
    # check if the hypothesis value contradicts the estimate of less than 'distance_traveled_premise'
    label = "contradiction"
elif distance_traveled_hypothesis == distance_traveled_premise:
    # check if the hypothesis value is equal to the estimate of less than 'distance_traveled_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance traveled
    # any distance traveled less than 'distance_traveled_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)