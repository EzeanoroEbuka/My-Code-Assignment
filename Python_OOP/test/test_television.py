from pythonSecondProject.television import Television


def test_television_can_come_on():
    my_tv = Television()
    my_tv.turn_on()
    assert my_tv.check_on_off() == True


def test_television_can_be_turned_off():
    my_tv = Television()
    my_tv.turn_on()
    my_tv.turn_off()
    assert my_tv.check_on_off() == False


def test_to_get_television_current_channel():
    my_tv = Television()
    my_tv.turn_on()
    assert my_tv.current_channel() == 1


def test_television_can_next_channel():
    my_tv = Television()
    my_tv.turn_on()
    my_tv.next_channel()
    assert my_tv.current_channel() == 2


def test_television_can_next_to_any_specified_channel():
    my_tv = Television()
    my_tv.turn_on()
    my_tv.to_channel(24)
    assert my_tv.current_channel() == 24


def test_television_can_return_to_previous_channel():
    my_tv = Television()
    my_tv.turn_on()
    my_tv.to_channel(15)
    assert my_tv.current_channel() == 15
    my_tv.previous_channel()
    assert my_tv.current_channel() == 14