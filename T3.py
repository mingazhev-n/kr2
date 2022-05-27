import threading


class mylist:
    def __init__(self, num):
        self.num = num
        self.data = []

    def get(self, copy=True):
        if copy:
            q = self.data
            return q
        else:
            return self.data

    def d_end(self, element):
        q = self.data
        try:
            if isinstance(element, float) or isinstance(element, int):
                q.append(element)
                return q
            elif isinstance(element, list):
                q = q + element
                return q
        except ValueError:
            print("Ошибка")

    def add_begin(self, element):
        q = self.data
        try:
            if isinstance(element, float) or isinstance(element, int):
                q = [element] + q
                return q
            elif isinstance(element, list):
                q = element + q
                return q
        except ValueError:
            print("Ошибка")

    def full_convert(self, _type):
        q = self.data
        d = {}
        try:
            if isinstance(_type, set):
                return set(q)
            elif isinstance(_type, tuple):
                return tuple(q)
            elif isinstance(_type, dict):
                d = {a: q[a] for a in range(len(q))}
                return d
            elif isinstance(_type, list):
                print(mylist.get(q))
        except ValueError:
            print("Ошибка")

    def set_parallel(func, *ar, **kwar):
        thr1 = threading.Thread(target=func, args=ar, kwargs=kwar).start()
        return thr1

    def wait_parallel(obj):
        pass
