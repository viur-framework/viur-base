from viur.core.modules.user import User


class User(User):
    """
    Customization of the default user module.
    """

    # Extend default adminInfo to custom adminInfo
    adminInfo = User.adminInfo | {
        "columns": [
            "name",
            "firstname",
            "lastname",
        ],
        "filter": {
            "orderby": "lastname",
        },
    }
