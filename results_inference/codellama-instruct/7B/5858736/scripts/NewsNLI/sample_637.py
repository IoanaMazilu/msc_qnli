def main():
    premise = "On it she had quickly scrawled two words:'' It's over.''"
    hypothesis = "Lawyer's two words told him his fate:'' It's over''"

    # extract the relevant information from the premise and hypothesis
    words_premise = "It's over"
    words_hypothesis = "It's over"

    # compare the extracted information
    if words_hypothesis!= words_premise:
        # the hypothesis mentions different words than the premise, which contradicts the premise
        label = "contradiction"
    else:
        # if the hypothesis mentions the same words as the premise, we can infer entailment
        label = "entailment"

    print(label)

if __name__ == "__main__":
    main()
