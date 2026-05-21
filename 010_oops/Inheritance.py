
class A:

    id = 10

    def test(self):
        print("Class A test calling")


class B(A):
    id = 50
    def sample(self):
        print(self.id)
        print(super().id)

# class C(B):
#     pass

# class C(A,B):
#     pass


# class C(A):
#     pass

# b = B()
# b.sample()
# b.test()