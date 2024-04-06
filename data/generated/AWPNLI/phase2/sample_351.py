# Premise: In 1.0 week, an airplane pilot flew 1134.0 miles on Tuesday and 1475.0 miles on Thursday, and the pilot flies the same number of miles 3.0 weeks in a row.
# Hypothesis: The pilot flew 7823.0 miles.
# Golden Label: contradiction

tuesday_miles_premise = 1134.0
thursday_miles_premise = 1475.0
weeks_premise = 3.0
total_miles_hypothesis = 7823.0

# the hypothesis refers to the total number of miles flown, which is also mentioned in the premise
# compute the total number of miles flown in the premise
total_miles_premise = (tuesday_miles_premise + thursday_miles_premise) * weeks_premise
if total_miles_hypothesis != total_miles_premise:
    # check if the total number of miles in the hypothesis contradicts the total number of miles from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

