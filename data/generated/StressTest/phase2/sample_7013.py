# Premise: Susan drove an average speed of 30 miles per hour for the first 60 miles of a tripthen at a average speed of 60 miles/hr for the remaining 30 miles of the trip if she made no stops during the trip what was susan's avg speed in miles/hr for the entire trip.
# Hypothesis: Susan drove an average speed of more than 30 miles per hour for the first 60 miles of a tripthen at a average speed of 60 miles/hr for the remaining 30 miles of the trip if she made no stops during the trip what was susan's avg speed in miles/hr for the entire trip.
# Golden Label: contradiction

avg_speed_first_part_premise = 30
avg_speed_first_part_hypothesis = 30
avg_speed_second_part_premise = 60
avg_speed_second_part_hypothesis = 60
distance_first_part = 60
distance_second_part = 30

# the hypothesis talks about the average speed Susan drove for the first and the second part of the trip
if avg_speed_first_part_hypothesis <= avg_speed_first_part_premise:
    # check if the hypothesis value contradicts the estimate of more than 'avg_speed_first_part_premise'
    label = "contradiction"
elif avg_speed_second_part_hypothesis != avg_speed_second_part_premise:
    # check if the average speed for the second part of the trip in the hypothesis contradicts the average speed for the second part of the trip reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

