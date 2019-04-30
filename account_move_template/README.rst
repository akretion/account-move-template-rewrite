.. image:: https://img.shields.io/badge/license-AGPL--3-blue.png
   :target: https://www.gnu.org/licenses/agpl
   :alt: License: AGPL-3

=====================
Account Move Template
=====================

The user can configure journal entries templates, useful for recurring entries.
The amount of each template line can be computed (through python code)
or kept as user input.

If user input, when using the template, user has to fill
the amount of every input lines.

The journal entry form allows lo load, through a wizard,
the template to use and the amounts to fill.

This version of the module is a backport of the rewrite of the module made by Alexis de Lattre for Odoo v12 in `this pull request <https://github.com/OCA/account-financial-tools/pull/801>`_. It is an alternative to the original version of the OCA available `here <https://github.com/OCA/account-financial-tools/tree/10.0/account_move_template>`_. Compared to the original version of the OCA, this module has several advantages:

#. proper handling of date and ref in the wizard,
#. use *float_round()* to avoid floats such as 3.666666666 in credit or debit (easy to achieve with type = compute), which can lead to big problems in Odoo's accounting (for example : in a balance with all accounts, total of credit may be different from total of debit !)
#. improved usability,
#. cleaner, simpler and easier code.

Usage
=====

To create new templates:

#. Make sure that the user belongs to the *Accounting Manager* group.
#. Go to *Accounting / Configuration / Accounting / Journal Entry Templates* and
   define there your templates. You can choose to complete a line using a
   defined formula, based on other lines, or by requiring user input.

To use an existing template:

#. Go to *Accounting / Adviser / Create Entry from Template*
#. Select one of the available templates.
#. Complete the entries according to the template and click on the button *Generate Journal Entry*.
