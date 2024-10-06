class calculator():
    def sum(self, *args):
        res = 0
        for i in args:
            res += i
        print(res)


# a = calculator()
# a.sum(2,4,5)