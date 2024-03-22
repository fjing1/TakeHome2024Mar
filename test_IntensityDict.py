from IntensityDict import IntensityDict

def test_add_1st():
    intensityDict = IntensityDict()
    intensityDict.add(10, 30, 1)
    assert intensityDict.get_intensities_dict() == [(10, 1), (30, 0)]

    intensityDict.add(20, 40, 1)
    assert intensityDict.get_intensities_dict() == [(10, 1), (20, 2), (30, 1), (40, 0)]

    intensityDict.add(10, 40, -2)
    assert intensityDict.get_intensities_dict() == [(10, -1), (20, 0), (30, -1), (40, 0)]
    intensityDict.clear()
    print("completed test set 1 for add")

def test_add_2nd():
    intensityDict = IntensityDict()
    intensityDict.add(10, 30, 1)
    assert intensityDict.get_intensities_dict() == [(10, 1), (30, 0)]
    intensityDict.add(20, 40, 1)
    assert intensityDict.get_intensities_dict() == [(10, 1), (20, 2), (30, 1), (40, 0)]

    intensityDict.add(10, 40, -1)
    assert intensityDict.get_intensities_dict() == [(20, 1), (30, 0)]
    intensityDict.add(10, 40, -1)
    assert intensityDict.get_intensities_dict() == [(10, -1), (20, 0),(30, -1), (40, 0)]
    print("completed test set 2 for add")

def test_set_default():
    intensityDict = IntensityDict()
    intensityDict.set(1, 5, 2)
    assert intensityDict.get_intensities_dict() == [(1, 2), (5, 0)]

def test_add_set():
    intensityDict = IntensityDict()
    intensityDict.add(10, 30, 1)
    assert intensityDict.get_intensities_dict() == [(10, 1), (30, 0)]
    intensityDict.set(10, 20, 2)
    assert intensityDict.get_intensities_dict() == [(10, 2), (20, 0)]
    intensityDict.set(0, 40, 0)
    assert intensityDict.get_intensities_dict() == []

print("start testing")
test_add_1st()
test_add_2nd()
test_set_default()
test_add_set()
print("testing completed")