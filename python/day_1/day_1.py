def sol_part_1(inp: str) -> int:

    vals = [int(x) for x in inp.split("\n")]

    for ind, val_1 in enumerate(vals):
        for val_2 in vals[ind + 1 :]:

            if val_1 + val_2 == 2020:
                return val_1 * val_2
            else:
                pass

    return None


def sol_part_2(inp: str) -> int:

    vals = [int(x) for x in inp.split("\n")]

    for ind_1, val_1 in enumerate(vals):
        for ind_2, val_2 in enumerate(vals[ind_1 + 1 :]):
            for val_3 in vals[ind_2 + 1 :]:

                if val_1 + val_2 + val_3 == 2020:
                    return val_1 * val_2 * val_3
                else:
                    pass

    return None


if __name__ == "__main__":

    with open("./day_1/part_1_input") as f:
        inp = f.read()

    res = sol_part_1(inp)
    print(f"part 1: {res}")

    res = sol_part_2(inp)
    print(f"part 2: {res}")