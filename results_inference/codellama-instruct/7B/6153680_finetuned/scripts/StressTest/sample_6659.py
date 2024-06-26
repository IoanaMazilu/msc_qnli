Karen_speed = 60
Tom_speed = 45
Q_miles = 100

# the hypothesis refers to the same situation as the premise, but with different speeds
Karen_speed_hyp = 70
Tom_speed_hyp = 45

# calculate the number of miles Tom will drive before Karen wins the bet
Tom_miles = Q_miles / (Karen_speed_hyp - Tom_speed_hyp)

# check if the hypothesis value contradicts the premise
if Tom_miles!= Tom_miles:
    label = "contradiction"
else:
    label = "neutral"

print(label)
