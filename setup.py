from setuptools import setup
import os
from glob import glob

package_name = 'forost_examples'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, "launch"), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, "trees"), glob('trees/*.xml')),
        
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pc',
    maintainer_email='patrick@coenenmail.de',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'condition_failure = forost_examples.condition_failure:main',
            'condition_success = forost_examples.condition_success:main',
            'action = forost_examples.action:main'
        ],
    },
)
