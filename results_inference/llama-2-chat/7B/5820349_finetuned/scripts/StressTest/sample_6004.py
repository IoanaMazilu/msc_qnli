balls_needed_premise = 3
balls_needed_hypothesis = 4
total_balls = 10

# the hypothesis refers to the number of balls John needs, which is also mentioned in the premise
if balls_needed_hypothesis <= balls_needed_premise:
    # check if the number of balls John needs in the hypothesis contradicts the premise estimate of more than 'balls_needed_premise'
    label = "contradiction"
elif balls_needed_hypothesis > total_balls:
    # check if the number of balls John needs in the hypothesis is greater than the total number of balls
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of balls John needs
    # any number of balls greater than 'balls_needed_premise' and less than or equal to 'total_balls' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
