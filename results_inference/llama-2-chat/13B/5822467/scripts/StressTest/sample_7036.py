fred_speed_premise = 8 # constant speed of less than 8 miles per hour
fred_speed_hypothesis = 5 # constant speed of 5 miles per hour
sam_speed_premise = 5 # constant speed of 5 miles per hour

# the hypothesis talks about the speed of both Fred and Sam, referenced also in the premise
if fred_speed_hypothesis <= fred_speed_premise and sam_speed_hypothesis == sam_speed_premise:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
elif fred_speed_hypothesis!= fred_speed_premise or sam_speed_hypothesis!= sam_speed_premise:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of both Fred and Sam
    # any speed consistent with the premise is consistent with the hypothesis
    label = "neutral"

print(label)
