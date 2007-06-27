from setuptools import setup, find_packages
import sys, os

if sys.version_info < (2, 3):
    raise SystemExit("Python 2.3 or later is required")

execfile(os.path.join("tg", "release.py"))

setup(
    name='TurboGears2',
    version=version,
    description=description,
    long_description=long_description,
    classifiers=[],
    keywords='turbogears pylons',
    author=author,
    author_email=email,
    url=url,
    license=license,
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'PasteScript>=1.3',
        'Pylons>0.9.5'
    ],
    entry_points='''
        [paste.paster_create_template]
        turbogears2=tg.pastetemplate:TurboGearsTemplate
        [paste.global_paster_command]
        quickstart = tg.command.quickstart:quickstart
    ''',
)