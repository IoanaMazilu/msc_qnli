_HIDDEN
    first_hours_premise = 80
    first_hours_hypothesis = 30
    additional_hours_premise = 2
    additional_hours_hypothesis = 2
    _HIDDEN

    # _HIDDEN
    if first_hours_hypothesis >= first_hours_premise:
        # check if the number of first hours in the hypothesis contradicts the estimate of less than 'first_hours_premise'
        label = "contradiction"
    elif additional_hours_hypothesis!= additional_hours_premise:
        # check if the number of additional hours in the hypothesis contradicts the number of additional hours reported in the premise
        label = "contradiction"
    else:
        # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
        label = "entailment"

    return [label]
    
