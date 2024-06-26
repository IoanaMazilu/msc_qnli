# define variables for the average speeds and the distance to be driven
karens_speed_premise = 60
karens_speed_hypothesis = 20
toms_speed_premise = 45
toms_speed_hypothesis = 45
distance_to_win_bet_premise = 100
distance_to_win_bet_hypothesis = 100

# calculate the time taken by Karen and Tom to drive the distance to win the bet
time_taken_karen_premise = distance_to_win_bet_premise / karens_speed_premise
time_taken_karen_hypothesis = distance_to_win_bet_hypothesis / karens_speed_hypothesis
time_taken_tom_premise = distance_to_win_bet_premise / toms_speed_premise
time_taken_tom_hypothesis = distance_to_win_bet_hypothesis / toms_speed_hypothesis

# calculate the total distance driven by Tom before Karen wins the bet
distance_driven_tom_premise = time_taken_tom_premise * toms_speed_premise
distance_driven_tom_hypothesis = time_taken_tom_hypothesis * toms_speed_hypothesis

# compare the total distance driven by Tom before Karen wins the bet
if distance_driven_tom_premise <= distance_driven_tom_hypothesis:
    # check if the estimate of 'distance_driven_tom_hypothesis' contradicts the total distance driven by Tom in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the total distance driven by Tom
    # any total distance driven by Tom greater than 'distance_driven_tom_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
