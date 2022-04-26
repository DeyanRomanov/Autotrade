def _get_max_choices_length(value):
    max_length = max([len(x[0]) for x in value])
    return max_length