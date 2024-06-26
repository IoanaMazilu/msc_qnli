x_per_hour_premise = 0 # initialize variable for premise
x_per_hour_hypothesis = 0 # initialize variable for hypothesis

# extract values from premise and hypothesis
for sentence in ["Each week, James is paid x dollars per per hour for the first 40 hours and 2 x dollars for each additional hour worked that week.", "Each week, James is paid x dollars per per hour for the first less than 60 hours and 2 x dollars for each additional hour worked that week."]:
    sentence_parts = sentence.split(" dollars per per hour")
    x_per_hour_premise = int(sentence_parts[1]) # extract value from premise
    x_per_hour_hypothesis = int(sentence_parts[1]) # extract value from hypothesis

# compare values
if x_per_hour_premise <= x_per_hour_hypothesis:
    # check if the estimate of 'x_per_hour_hypothesis' contradicts the number of hours worked in the premise
    label = "contradiction"
elif x_per_hour_hypothesis < x_per_hour_premise:
    # check if the number of hours worked in the hypothesis contradicts the number of hours worked in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
