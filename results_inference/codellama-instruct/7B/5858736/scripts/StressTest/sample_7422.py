albert_elevator_premise = 51
albert_elevator_hypothesis = 61
albert_elevator_rate = 63

if albert_elevator_hypothesis >= albert_elevator_premise:
    label = "contradiction"
elif albert_elevator_rate!= 63:
    label = "contradiction"
else:
    label = "neutral"

print(label)
