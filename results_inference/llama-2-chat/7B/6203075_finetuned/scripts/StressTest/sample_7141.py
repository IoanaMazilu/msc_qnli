# the premise and hypothesis are asking about the number of subsequent flights that need to depart on time
# from the same airport, given that the next three flights have departed on time

# the hypothesis refers to a higher on-time departure rate than 40%
# the premise refers to a higher on-time departure rate than 40%

if hypothesis[1]!= premise[1]:
    # check if the on-time departure rate in the hypothesis contradicts the on-time departure rate in the premise
    label = "contradiction"
elif hypothesis[0]!= premise[0]:
    # check if the number of flights in the hypothesis contradicts the number of flights in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
