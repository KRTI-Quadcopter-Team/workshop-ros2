from setuptools import find_packages, setup

package_name = 'simulation_packages'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
            "gui_status = simulation_packages.gui_status:main",
            "mavros_sim = simulation_packages.mavros_sim:main"
        ],
    },
)
