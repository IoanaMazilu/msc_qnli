# Premise: Assuming that Karen drives at an average speed of 60 mph and Tom drives at an average speed of 45 mph, how many Q miles will Tom drive before Karen wins the bet?
# Hypothesis: Assuming that Karen drives at an average speed of less than 80 mph and Tom drives at an average speed of 45 mph, how many Q miles will Tom drive before Karen wins the bet?
# Golden Label: entailment

karen_speed_premise = 60
karen_speed_hypothesis = 80
tom_speed_premise = 45
tom_speed_hypothesis = 45

# the hypothesis refers to the driving speed of Karen and Tom mentioned in the premise
if karen_speed_premise >= karen_speed_hypothesis:
    # check if the estimate of 'karen_speed_hypothesis' contradicts the speed of Karen in the premise
    label = "contradiction"
elif tom_speed_premise != tom_speed_hypothesis:
    # check if the speed of Tom in the hypothesis contradicts the speed of Tom mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
