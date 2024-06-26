course_length_premise = 300
course_length_hypothesis = 600
teams_premise = 2
teams_hypothesis = 2

# the hypothesis talks about the length of a course and the number of dogsled teams, both mentioned in the premise
if course_length_hypothesis != course_length_premise:
    # check if the course length in the hypothesis contradicts the course length reported in the premise
    label = "contradiction"
elif teams_hypothesis != teams_premise:
    # check if the number of teams in the hypothesis contradicts the number of teams reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
