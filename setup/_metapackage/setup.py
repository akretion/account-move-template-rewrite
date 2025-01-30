import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo10-addons-akretion-account-move-template-rewrite",
    description="Meta package for akretion-account-move-template-rewrite Odoo addons",
    version=version,
    install_requires=[
        'odoo10-addon-account_move_template',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 10.0',
    ]
)
