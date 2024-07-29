from ConcreateFactories.ConcreateFactories import RawabiConcreateFactory


def rawabi_running_code(factory):
    rawabi_parser = factory.parser_base()
    return rawabi_parser.parser_function()


def pick_parser(type_name):
    if type_name == "RawabiType":
        return rawabi_running_code(RawabiConcreateFactory())


if __name__ == "__main__":
    Rawabi_Type = "RawabiType"

    Rawabi_Type_receipt = pick_parser(Rawabi_Type)
