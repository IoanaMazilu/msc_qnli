# define variables for the premise and hypothesis
premise = "Perhaps the St. Andrews New Course (greens fee, $110), a tough-as-nails layout with the fastest greens in town, might be thrown in for good measure."
hypothesis = "St. Andrews Links Trust manages seven courses in and around the town."

# extract the numerical entities from the premise
greens_fee = 110

# extract the numerical entities from the hypothesis
number_of_courses = 7

# compare the number of courses in the hypothesis to the number of courses in the premise
if number_of_courses!= 1:
    # if the number of courses in the hypothesis contradicts the number of courses in the premise, we can infer contradiction
    label = "contradiction"
else:
    # if the number of courses in the hypothesis does not contradict the number of courses in the premise, we can infer neutral
    label = "neutral"

print(label)
