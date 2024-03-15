from IntensityManager import IntensityManager

def test_add_1st():
    manager = IntensityManager()
    # Test add method with 1st test case
    manager.add(10, 30, 1)
    #print(manager.intensities, "expected to be [(10, 1), (30, 0)]")
    assert manager.get_turning_point_intensities() == [(10, 1), (30, 0)]

    manager.add(20, 40, 1)
    #print(manager.intensities)
    assert manager.get_turning_point_intensities() == [(10, 1), (20, 2), (30, 1), (40, 0)]

    manager.add(10, 40, -2)
    print(manager.get_turning_point_intensities())
    assert manager.get_turning_point_intensities() == [(10, -1), (20, 0), (30, -1), (40, 0)]
    manager.clear()

def test_add_2nd():
    manager = IntensityManager()
    # Test add method with 2nd test case
    manager.add(10, 30, 1)
    print(manager.get_turning_point_intensities())
    assert manager.get_turning_point_intensities() == [(10, 1), (30, 0)]
    manager.add(20, 40, 1)
    assert manager.get_turning_point_intensities() == [(10, 1), (20, 2), (30, 1), (40, 0)]

    manager.add(10, 40, -1)
    print(manager.get_turning_point_intensities())
    assert manager.get_turning_point_intensities() == [(20, 1), (30, 0)]
    manager.add(10, 40, -1)
    print(manager.get_turning_point_intensities())
    assert manager.get_turning_point_intensities() == [(10, -1), (20, 0),(30, -1), (40, 0)]

print("start testing")
test_add_1st()
test_add_2nd()