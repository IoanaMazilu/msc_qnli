# Premise: Gwen drove an average speed of 15 miles per hour for the first 40 miles of a tripthen at a average speed of 30 miles/hr for the remaining 40 miles of the trip if she made no stops during the trip what was Gwen's avg speed in miles/hr for the entire trip.
# Hypothesis: Gwen drove an average speed of less than 15 miles per hour for the first 40 miles of a tripthen at a average speed of 30 miles/hr for the remaining 40 miles of the trip if she made no stops during the trip what was Gwen's avg speed in miles/hr for the entire trip.
# Golden Label: contradiction

avg_speed_first_part_premise = 15
avg_speed_first_part_hypothesis = 15
avg_speed_second_part_premise = 30
avg_speed_second_part_hypothesis = 30

# the hypothesis refers to the average speed of Gwen's trip and the premise also provides this information
if avg_speed_first_part_hypothesis >= avg_speed_first_part_premise:
    # check if the hypothesis value contradicts the average speed for the first part of the trip from the premise
    label = "contradiction"
elif avg_speed_second_part_hypothesis != avg_speed_second_part_premise:
    # check if the average speed for the second part of the trip in the hypothesis contradicts the one reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

