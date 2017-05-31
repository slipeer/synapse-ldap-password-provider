# __init__.py
from synapse_ldap_password_provider import LDAPPasswordProvider


def create_auth_provider(port, account_handler):
    "Creates an LDAPPasswordProvider from an LDAP server and a mock account_handler"

    config = LDAPPasswordProvider.parse_config({
        "enabled": True,
        "uri": "ldap://localhost:%s" % port,
        "base": "ou=people,dc=example,dc=org",
        "attributes": {
            "uid": "cn",
            "name": "gn",
            "mail": "mail",
        },
    })

    return LDAPPasswordProvider(config, account_handler=account_handler)
