from setuptools import find_packages, setup

package_name = 'robot_movement'

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
    maintainer='eduardo',
    maintainer_email='eduardo.montalvo12@hotmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "Movement_exec = robot_movement.node_movement:main",
            "Messager = robot_movement.velocity_publisher:main"
        ],
    },
)
