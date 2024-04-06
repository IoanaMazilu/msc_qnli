# Premise: You want to give 24.0 cookies to each of the 6.0 people.
# Hypothesis: You need 145.0 cookies.
# Golden Label: contradiction

cookies_each_person_premise = 24.0
people_premise = 6.0
total_cookies_hypothesis = 145.0

# the hypothesis refers to the total number of cookies, which is also referenced in the premise
# compute the total number of cookies in the premise
total_cookies_premise = cookies_each_person_premise * people_premise
if total_cookies_hypothesis != total_cookies_premise:
    # check if the total number of cookies in the hypothesis contradicts the total number of cookies from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

