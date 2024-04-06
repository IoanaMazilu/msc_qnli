# Premise: You want to give 24.0 cookies to each of the 6.0 people.
# Hypothesis: You need 144.0 cookies.
# Golden Label: entailment

cookies_per_person_premise = 24.0
people_premise = 6.0
total_cookies_hypothesis = 144.0

# the hypothesis refers to the total number of cookies, which can be computed from the premise
# compute the total number of cookies in the premise
total_cookies_premise = cookies_per_person_premise * people_premise
if total_cookies_hypothesis != total_cookies_premise:
    # check if the total number of cookies in the hypothesis contradicts the total number of cookies from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

