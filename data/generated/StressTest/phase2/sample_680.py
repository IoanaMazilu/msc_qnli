# Premise: City A to city B, Raja drove for 1 hour at 72 mph and for 3 hours at 80 mph.
# Hypothesis: City A to city B, Raja drove for 6 hour at 72 mph and for 3 hours at 80 mph.
# Golden Label: contradiction

# Speed and time for the first part of Raja's trip from city A to city B
speed_city_A_B_part1_premise = 72
time_city_A_B_part1_premise = 1

# Speed and time for the second part of Raja's trip from city A to city B
speed_city_A_B_part2_premise = 80
time_city_A_B_part2_premise = 3

# Speed and time for the first part of Raja's trip from city A to city B according to the hypothesis
speed_city_A_B_part1_hypothesis = 72
time_city_A_B_part1_hypothesis = 6

# Speed and time for the second part of Raja's trip from city A to city B according to the hypothesis
speed_city_A_B_part2_hypothesis = 80
time_city_A_B_part2_hypothesis = 3

# The hypothesis talks about the same trip from city A to city B that is described in the premise
if speed_city_A_B_part1_premise != speed_city_A_B_part1_hypothesis or time_city_A_B_part1_premise != time_city_A_B_part1_hypothesis:
    # Check if the speed or the time for the first part of the trip in the hypothesis contradicts the speed or the time for the first part of the trip in the premise
    label = "contradiction"
elif speed_city_A_B_part2_premise != speed_city_A_B_part2_hypothesis or time_city_A_B_part2_premise != time_city_A_B_part2_hypothesis:
    # Check if the speed or the time for the second part of the trip in the hypothesis contradicts the speed or the time for the second part of the trip in the premise
    label = "contradiction"
else:
    # If the speeds and times for both parts of the trip in the hypothesis do not contradict the speeds and times for both parts of the trip in the premise, we can infer entailment
    label = "entailment"

print(label)

