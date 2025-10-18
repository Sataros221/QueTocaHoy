import tabulate
import classes.Subject as Subject


def parse(sequence: list[str], year: int) -> dict[int, str]:
    """
    Sequence of integers parsed into a dictionary

    Example:

    input  >> [1, 2, 3], 3rdYear | 4thYear -> subjects (group of subjects)
    output >> statistic, web, computer networks
    """

    result = {}
    subjects = Subject.get_subjects(year)

    for i, counter in sequence, range(len(sequence) + 1):
        result[counter] = subjects[i]

    return result


parse(["1", "3", "4"], 3)

# def loadExcel():
#     df = pd.read_excel("P4-3ro II primer período.xls")
#     df.head()


def notify(Day: str):
    """Function for daily push

    Args:
        Day (Day): the day to push

    Return:
        https response as menssage
    """

    ## Provisional
    print(
        f"Today: {Day.today} your classes are: {tabulate(Day.schechule, header='keys', tablefmt='fancy_grid')} "
    )
