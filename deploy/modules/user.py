from viur.core.modules.user import User as User


class User(User):
    """
    Customization of the default user module.
    """

    # Extend default adminInfo to custom adminInfo
    adminInfo = User.adminInfo | {
        "columns": ["lastname", "firstname", "name"],
        "filter": {"orderby": "lastname"},
    }
