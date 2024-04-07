# Premise: Xavier starts from P towards Q at a speed of more than 10 kmph and after every 12 mins increases his speed by 20 kmph.
# Hypothesis: Xavier starts from P towards Q at a speed of 90 kmph and after every 12 mins increases his speed by 20 kmph.
# Golden Label: neutral

initial_speed_premise = 10
initial_speed_hypothesis = 90
time_interval = 12  # in minutes
speed_increase = 20  # in kmph

# the hypothesis refers to Xavier's starting speed and speed increase mentioned in the premise
if initial_speed_hypothesis <= initial_speed_premise:
    # check if the initial speed in the hypothesis contradicts the premise stating the initial speed is more than 'initial_speed_premise' kmph
    label = "contradiction"
else:
    # the premise gives only a lower limit for the starting speed
    # any starting speed greater than 'initial_speed_premise' kmph is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

