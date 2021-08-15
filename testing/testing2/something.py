class Something:
    def __init__(self, parent):
        print(getattr(parent,'something'))
