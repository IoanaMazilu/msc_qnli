# Premise: Susan drove an average speed of 30 miles per hour for the first 60 miles of a tripthen at a average speed of 60 miles/hr for the remaining 30 miles of the trip if she made no stops during the trip what was susan's avg speed in miles/hr for the entire trip.
# Hypothesis: Susan drove an average speed of less than 80 miles per hour for the first 60 miles of a tripthen at a average speed of 60 miles/hr for the remaining 30 miles of the trip if she made no stops during the trip what was susan's avg speed in miles/hr for the entire trip.
# Golden Label: entailment

avg_speed_premise_first_part = 30
avg_speed_hypothesis_first_part = 80
avg_speed_premise_second_part = 60
avg_speed_hypothesis_second_part = 60

# the hypothesis refers to the average speeds during the first and the second part of the trip, as mentioned in the premise
if avg_speed_premise_first_part >= avg_speed_hypothesis_first_part:
    # check if the average speed in the first part of the trip in the hypothesis contradicts the average speed mentioned in the premise
    label = "contradiction"
elif avg_speed_hypothesis_second_part != avg_speed_premise_second_part:
    # check if the average speed in the second part of the trip in the hypothesis contradicts the average speed mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, but the premise does not fully entail the hypothesis 
    label = "neutral"

print(label)

