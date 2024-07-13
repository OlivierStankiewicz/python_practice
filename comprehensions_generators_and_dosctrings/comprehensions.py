def comprehensionTypes() -> None:
    dict_comp = {i: i*i for i in range(10)}
    list_comp = [i*i for i in range(10)]
    set_comp = {i%3 for i in range(10)}
    gen_comp = (2*i+5 for i in range(10))