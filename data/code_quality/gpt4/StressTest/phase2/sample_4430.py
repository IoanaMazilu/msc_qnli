list_requirement_premise = 1/4
list_requirement_hypothesis = 3/4
members_academy = 765

# both the hypothesis and the premise state the requirement for a movie to be considered "movie of the year"
if list_requirement_hypothesis < list_requirement_premise:
    # check if the requirement in the hypothesis contradicts the requirement stated in the premise
    label = "contradiction"
elif list_requirement_hypothesis == list_requirement_premise:
    # if the requirements in both the hypothesis and the premise match, we can infer entailment
    label = "entailment"
else:
    # any requirement larger than 'list_requirement_premise' does not contradict the premise, but cannot be explicitly entailed from it
    label = "neutral"

print(label)
