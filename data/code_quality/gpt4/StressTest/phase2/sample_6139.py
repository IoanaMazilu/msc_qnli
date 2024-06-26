travel_time_premise = 4
travel_time_hypothesis = 7

# The hypothesis talks about the total time taken by Kiran to travel from A to B and back, which is also mentioned in the premise
if travel_time_hypothesis <= travel_time_premise:
    # Check if the stated travel time in the hypothesis contradicts the estimate of more than 'travel_time_premise' 
    label = "contradiction"
else:
    # The premise gives only an estimate for the travel time
    # Any travel time greater than 'travel_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
