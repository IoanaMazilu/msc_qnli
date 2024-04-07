# Premise: Susan drove an average speed of 15 miles per hour for the first 40 miles of a tripthen at a average speed of 60 miles/hr for the remaining 20 miles of the trip if she made no stops during the trip what was susan's avg speed in miles/hr for the entire trip.
# Hypothesis: Susan drove an average speed of more than 15 miles per hour for the first 40 miles of a tripthen at a average speed of 60 miles/hr for the remaining 20 miles of the trip if she made no stops during the trip what was susan's avg speed in miles/hr for the entire trip.
# Golden Label: contradiction

average_speed_premise_first_leg = 15
average_speed_hypothesis_first_leg = 15
average_speed_premise_second_leg = 60
average_speed_hypothesis_second_leg = 60

# the hypothesis refers to the average speeds of two legs of the trip mentioned in the premise
if average_speed_hypothesis_first_leg <= average_speed_premise_first_leg:
    # check if the value of 'average_speed_hypothesis_first_leg' contradicts the average speed in the first leg of the trip in the premise
    label = "contradiction"
elif average_speed_hypothesis_second_leg != average_speed_premise_second_leg:
    # check if the average speed in the second leg of the trip in the hypothesis contradicts the average speed in the second leg of the trip reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average speeds
    # any average speed greater than 'average_speed_premise_first_leg' and 'average_speed_premise_second_leg' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

