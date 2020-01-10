class Segment:

    def __init__(self):
        self.a = 0
        self.b = 0
        self.empty = True

    def make_segment_empty(self):
        self.a = 0
        self.b = 0
        self.empty = True

    def is_empty(self):
        if self.empty:
            return True
        return False

    def put_segment(self, a,b):
        self.a = a
        self.b = b
        self.empty = False
        return self

    def put_intersection(self, segment1, segment2):
        self.a = max(segment1.a, segment2.a)
        self.b = min(segment1.b, segment2.b)
        self.empty = False
        return self

    def print(self):
        print("Segment : [" + str(self.a) + " - " + str(self.b) + "]")


if __name__ == '__main__':
    s1 = Segment();
    s2 = Segment();
    s2.put_segment(10,20)

    print("Check if segment1 is Empty : ", s1.is_empty())
    print("Check if segment1 is Empty : ", s2.is_empty())

    s1.put_segment(9,22)

    s3 = Segment().put_intersection(s1,s2)
    s3.print()

    dct = {"Mike" : ['+', '-'],
           "Sasha" : ['-']
           }
    for el, arr in dct.items():
        if len(arr) != 2:
            arr.append('-')


    print('444')
    for el, arr  in dct.items():
        if len(dct.get(el, None)) == 3:
            print('44444444444444444444444444444')
        print(el,arr)
