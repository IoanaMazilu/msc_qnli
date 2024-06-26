first_week_premise = 5
first_week_hypothesis = 5
second_week_premise = 10
second_week_hypothesis = 10
third_week_premise = 20
third_week_hypothesis = 20
fourth_week_premise = 80
fourth_week_hypothesis = 80

# the hypothesis refers to the same number of cockroaches at each week mentioned in the premise
# except for the first week where the hypothesis suggests a number greater than the one in the premise
if first_week_hypothesis <= first_week_premise:
    # check if the hypothesis value contradicts the estimate of more than 'first_week_premise'
    label = "contradiction"
elif second_week_premise != second_week_hypothesis or third_week_premise != third_week_hypothesis or fourth_week_premise != fourth_week_hypothesis:
    # check if the number of cockroaches in the hypothesis contradicts the number of cockroaches reported in the premise for the other weeks
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of roses
    # any number of roses greater than 'first_week_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
