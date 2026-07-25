from schemas import CountryNumbersComparingResult


def country_numbers_comparing(overview_numbers: set[int], snapshot_numbers: set[int]) -> CountryNumbersComparingResult:
    """
    The function compars if the overview belongs to snapshot through country numbers

    Args:
        overview_numbers (set[int]): set of country numbers from the overview source file
        snapshot_numbers (set[int]): set of country numberf form the snapshot source file

    Returns:
        CountryNumbersComparingResult: ok and erorrs return
    """
    errors = []
    
    if not overview_numbers:
        return CountryNumbersComparingResult(
            ok=False,
            erorrs=["No country numbers from the overview parser"]
        )
    
    if not snapshot_numbers:
        return CountryNumbersComparingResult(
            ok=False,
            erorrs=["No country numbers from the snapshot parser"]
        )
        
    difference_in_numbers = overview_numbers - snapshot_numbers, snapshot_numbers - overview_numbers
    
    if difference_in_numbers[0] | difference_in_numbers[1]:
        return CountryNumbersComparingResult(
            ok=False,
            erorrs=["The country numbers are not the same. Found this differences:"] + difference_in_numbers
        )
    
    return CountryNumbersComparingResult(
        ok=True,
        erorrs=[]
    )