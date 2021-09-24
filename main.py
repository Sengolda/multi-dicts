class MultiDicts(list):
    def __init__(self, per_dict: int):
        self.per_dict = per_dict
        super().__init__()

    def append(self, __object) -> None:
        if not isinstance(__object, dict):
            raise RuntimeError("Objects appended to a MuliDicts list must be a dict.")
        return super().append(__object)

    def sort_dicts(self):
        for d in self:
            if len(d.keys()) >= self.per_dict:
                for k, elem in d.items():
                    _key = k
                    del d[_key]
                    new = dict()
                    new[k] = elem
                    self.append(new)
                    break
