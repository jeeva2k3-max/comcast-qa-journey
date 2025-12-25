class AssertionErrorCustom(Exception):
    pass


def assert_equal(actual, expected, message=""):
    if actual != expected:
        raise AssertionErrorCustom(
            f"ASSERT EQUAL FAILED | Expected: {expected}, Actual: {actual}. {message}"
        )


def assert_true(condition, message=""):
    if not condition:
        raise AssertionErrorCustom(
            f"ASSERT TRUE FAILED | Condition evaluated to False. {message}"
        )
