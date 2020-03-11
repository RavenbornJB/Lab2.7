from scale_zip import ScaleZip


if __name__ == '__main__':

    res = input("Enter resolution ('x' in the middle): ").split("x")

    if len(res) == 2 and res[0].isdigit() and res[1].isdigit():
        res = tuple(map(int, res))

    assert isinstance(res, tuple) and len(res) == 2

    sz = ScaleZip("2.zip", res)
    sz.process_zip()
