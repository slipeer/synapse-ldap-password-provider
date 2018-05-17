Synapse LDAP pasword provider
=============================

- Allows synapse to use LDAP database as a password provider.
- Allows to map mail and msisdn (phone) from LDAP (check usage note!). May be used in mxisd SynapseSQL backend.
- Allows implementing independent account lockout policy, to prevent Active Directory users locking by external bruteforce attack.
- Supports unicode characters in ldap DistinguishedName attributes
- Compatible with synapse 0.29.x

Travis-CI Build Status
======================
.. image:: https://travis-ci.org/slipeer/synapse-ldap-password-provider.svg?branch=master
    :target: https://travis-ci.org/slipeer/synapse-ldap-password-provider

Installation
------------

- Via python's package manager: `pip install synapse-ldap-password-provider`
- Via python's package manager from git: `pip install https://github.com/slipeer/synapse-ldap-password-provider/tarball/master`

Usage
-----

Example synapse config:

.. code:: yaml

   password_providers:
    - module: "synapse_ldap_password_provider.LDAPPasswordProvider"
      config:
        enabled: true
        uri: "ldap://ldap.example.com:389"
        start_tls: true
        base: "ou=users,dc=example,dc=com"
        attributes:
           uid: "samaccountname"
           name: "DisplayName"
           # Optional. Please read usage note!
           mail: "email"
           # Optional. Please read usage note!
           msisdn: "phone"
        #bind_dn:
        #bind_password:
        #filter: "(&(objectClass=user)(objectCategory=person))"
        # If you do not want your internal users to be blocked from outside
        # by scrambling passwords through this service, then you need
        # implement a more rigid account lockout policy then in yor LDAP server
        # This example user locks after 5 badd attemps to 5 minutes
        account_lockout_policy:
            locktime_s: 300
            attemps: 5


Do not use ``cn`` attribute as uid. It's common mistake: ``cn`` attribute not uniqe in LDAP tree in most schemas!
It's work fine only in very simple LDAP installations without complex Organizational Units structire.
You can use: ``samaccountname``, ``uid`` or ``userPrincipalName`` (depending on the schemes in your system). These attributes are always unique.

Usage note
----------

Use attributes ``mail`` and ``msisdn`` from the LDAP only if your identity server is also integrated with LDAP and looks for 3pd in these attributes.
Otherwise it will not work properly. If you seach identity server with LDAP integration you can try mxisd https://github.com/kamax-io/mxisd 
but unfortunately in has terribly slow implementation of bulk lookup for LDAP, do not cache queries and has no implementation for bulk_lookup for SQL backend.

Account Lockout Policy
----------------------
If you do not want your internal users to be blocked from outside by scrambling passwords through this service, then you need 
implement a more rigid account lockout policy then on your LDAP server.

Case Sensitivity
----------------
In most LDAP realizations login and email is case insensitive. But in matrix-org/synapse code matrixId and login is case sensitive (so user with login ``User`` can't auth with login ``USer``)
This ldap_auth_provider reduce user_id and email (i gues that phone number sonsist only froom digits) to lower case.
For this to work properly you may need to patch matrix-org/synapse with `<synapse.login_symbol_case_tolower.diff>`_


Troubleshooting and Debugging
-----------------------------

``synapse-ldap-password-provider`` logging is included in the Synapse homeserver log
(typically ``homeserver.log``). The LDAP plugin log level can be increased to
``DEBUG`` for troubleshooting and debugging by making the following modifications
to your Synapse server's logging configuration file:

- Set the value for `handlers.file.level` to `DEBUG`:

.. code:: yaml

   handlers:
     file:
       # [...]
       level: DEBUG

- Add the following to the `loggers` section:

.. code:: yaml

   loggers:
      # [...]
      ldap3:
        level: DEBUG
      ldap:
        level: DEBUG

Finally, restart your Synapse server for the changes to take effect:

.. code:: sh


   synctl restart

