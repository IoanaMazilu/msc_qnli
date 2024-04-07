# Premise: Susan drove an average speed of 15 miles per hour for the first 40 miles of a tripthen at a average speed of 60 miles/hr for the remaining 20 miles of the trip if she made no stops during the trip what was susan's avg speed in miles/hr for the entire trip.
# Hypothesis: Susan drove an average speed of less than 45 miles per hour for the first 40 miles of a tripthen at a average speed of 60 miles/hr for the remaining 20 miles of the trip if she made no stops during the trip what was susan's avg speed in miles/hr for the entire trip.
# Golden Label: entailment

average_speed_first_part_premise = 15
average_speed_first_part_hypothesis = 45
average_speed_second_part_premise = 60
average_speed_second_part_hypothesis = 60
miles_first_part = 40
miles_second_part = 20

# hypothesis refers to the average speed of Susan during the trip
if average_speed_first_part_hypothesis >= average_speed_first_part_premise:
    # check if the stated average speed in the hypothesis for the first part of the trip contradicts with the premise
    label = "contradiction"
elif average_speed_second_part_hypothesis != average_speed_second_part_premise:
    # check if the stated average speed in the hypothesis for the second part of the trip contradicts with the premise
    label = "contradiction"
else:
    # if the stated average speeds in the hypothesis does not contradict with the premise, we can infer entailment
    label = "entailment"

print(label)

