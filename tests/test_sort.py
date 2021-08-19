import utils.sort as s

RESULT = [
    {
        "Supplier": "Heaven Hill",
        "Brand Name": "Aristocrat Rum 80",
        "Proof": 80,
        "Bottle Size": ".75L",
        "Retail Bottle Price": 6.2,
        "Type": "Rum",
    },
    {
        "Supplier": "Sazerac Co.",
        "Brand Name": "Mr. Boston Light Rum",
        "Proof": 80,
        "Bottle Size": ".75L",
        "Retail Bottle Price": 6.15,
        "Type": "Rum",
    },
]


def test_sort():
    """
    Test filter_and_sort() function
    """
    sorted_result = s.filter_and_sort(RESULT, "Rum")
    assert sorted_result[0]["Retail Bottle Price"] == "6.15"
    assert sorted_result[1]["Retail Bottle Price"] == "6.20"


def test_decimals():
    """
    Test fix_decimals() function
    """
    result = s.fix_decimals(6.2)
    assert result == format(6.20, ".2f")
