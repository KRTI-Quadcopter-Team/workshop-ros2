import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'driver_packages'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='aftazani',
    maintainer_email='taftazani17@gmail.com',
    description='TODO: Package description',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "camera_driver = driver_packages.cam_driver_pub:main",
            "sensor_driver = driver_packages.sensor_driver_pub:main",
            "grip_driver = driver_packages.grip_driver_srv_pub:main"
        ],
    },
)
