# Premise: Susan drove an average speed of less than 45 miles per hour for the first 40 miles of a tripthen at a average speed of 60 miles/hr for the remaining 20 miles of the trip if she made no stops during the trip what was susan's avg speed in miles/hr for the entire trip.
# Hypothesis: Susan drove an average speed of 15 miles per hour for the first 40 miles of a tripthen at a average speed of 60 miles/hr for the remaining 20 miles of the trip if she made no stops during the trip what was susan's avg speed in miles/hr for the entire trip.
# Golden Label: neutral

avg_speed_first_40_miles_premise = 45
avg_speed_first_40_miles_hypothesis = 15
avg_speed_remaining_20_miles_premise = avg_speed_remaining_20_miles_hypothesis = 60

# Both premise and hypothesis talk about Susan's average speed for the first 40 miles and the remaining 20 miles of a trip

if avg_speed_first_40_miles_hypothesis >= avg_speed_first_40_miles_premise:
    # check if the hypothesis value contradicts the estimate of less than 'avg_speed_first_40_miles_premise'
    label = "contradiction"
elif avg_speed_remaining_20_miles_hypothesis != avg_speed_remaining_20_miles_premise:
    # check if the average speed for the remaining 20 miles in the hypothesis contradicts the same in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

