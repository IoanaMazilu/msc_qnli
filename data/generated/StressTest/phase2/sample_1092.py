# Premise: Susan drove an average speed of 30 miles per hour for the first 40 miles of a trip then at a average speed of 15 miles/hr for the remaining 40 miles of the trip if she made no stops during the trip what was susan's avg speed in miles/hr for the entire trip.
# Hypothesis: Susan drove an average speed of more than 20 miles per hour for the first 40 miles of a trip then at a average speed of 15 miles/hr for the remaining 40 miles of the trip if she made no stops during the trip what was susan's avg speed in miles/hr for the entire trip.
# Golden Label: entailment

first_leg_speed_premise = 30
first_leg_speed_hypothesis = 20
second_leg_speed_premise = 15
second_leg_speed_hypothesis = 15

# the hypothesis refers to the average speeds of two parts of a trip mentioned in the premise
if first_leg_speed_premise <= first_leg_speed_hypothesis:
    # check if the estimate of 'first_leg_speed_hypothesis' contradicts the number of speed in the first leg of the trip in the premise
    label = "contradiction"
elif second_leg_speed_hypothesis != second_leg_speed_premise:
    # check if the speed in the second leg of the trip in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

