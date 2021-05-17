from importlib import import_module


def model_from_string(model_name):

    return getattr(
        import_module(('.').join(model_name.split('.')[:-1])),
        model_name.rsplit(".")[-1],
    )()
