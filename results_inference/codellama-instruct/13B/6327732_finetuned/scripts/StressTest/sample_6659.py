# define variables for the numerical entities in the premise
karen_speed_premise = 60
tom_speed_premise = 45
distance_premise = 100

# define variables for the numerical entities in the hypothesis
karen_speed_hypothesis = 70
tom_speed_hypothesis = 45
distance_hypothesis = 100

# calculate the time taken by Karen to drive the distance
time_premise = distance_premise / karen_speed_premise
time_hypothesis = distance_hypothesis / karen_speed_hypothesis

# calculate the distance driven by Tom before Karen wins the bet
distance_premise = time_premise * tom_speed_premise
distance_hypothesis = time_hypothesis * tom_speed_hypothesis

# compare the distances driven by Tom before Karen wins the bet
if distance_premise <= distance_hypothesis:
    # check if the distance driven by Tom in the hypothesis contradicts the distance driven in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance driven by Tom
    # any distance driven by Tom greater than the distance driven in the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
