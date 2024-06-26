#week_premise = 1
#week_hypothesis = 5
#times_gym_premise = 3
#times_gym_hypothesis = 3

# the hypothesis refers to the number of weeks and the average number of times Rikki goes to the gym, both mentioned in the premise
# if the number of weeks in the hypothesis is the same as in the premise, but the average number of times Rikki goes to the gym is different, then it's a contradiction
# if the number of weeks in the hypothesis is more than the number of weeks in the premise, then it's a contradiction
# if the number of weeks in the hypothesis is less than the number of weeks in the premise, then it's a neutral case
# if the number of weeks in the hypothesis is the same as the number of weeks in the premise and the average number of times Rikki goes to the gym is the same, then it's an entailment

#if week_hypothesis == week_premise and times_gym_hypothesis!= times_gym_premise:
#    label = "contradiction"
#elif week_hypothesis > week_premise:
#    label = "contradiction"
#elif week_hypothesis < week_premise:
#    label = "neutral"
#else:
#    label = "entailment"

#print(label)
#