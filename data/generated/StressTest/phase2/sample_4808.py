# Premise: Bob can bake a pie in 6 minutes.
# Hypothesis: Bob can bake a pie in 4 minutes.
# Golden Label: contradiction

pie_baking_time_premise = 6
pie_baking_time_hypothesis = 4

# the hypothesis talks about the time Bob takes to bake a pie, referenced also in the premise
if pie_baking_time_hypothesis >= pie_baking_time_premise:
    # check if the time in the hypothesis contradicts the time mentioned in the premise
    label = "contradiction"
else:
    # the premise gives a specific time for baking a pie
    # any time less than 'pie_baking_time_premise' contradicts the premise
    label = "contradiction"

print(label)

