from viur.core.modules.user import User


class User(User):
    """
    Customization of the default user module.
    """

    # Extend default adminInfo with custom columns/filter.
    # viur-core 3.8 exposes adminInfo as a method (not a dict attribute),
    # so override and merge with super().adminInfo().
    def adminInfo(self) -> dict:
        return super().adminInfo() | {
            "columns": [
                "name",
                "firstname",
                "lastname",
            ],
            "filter": {
                "orderby": "lastname",
            },
        }
