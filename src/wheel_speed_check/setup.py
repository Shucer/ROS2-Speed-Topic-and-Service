from setuptools import find_packages, setup

package_name = 'wheel_speed_check'

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
    maintainer='shucer',
    maintainer_email='mounir.gharbi026@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'publisher = wheel_speed_check.wheel_speed_publisher:main',
            'subscriber = wheel_speed_check.wheel_speed_subscriber:main',
            'server = wheel_speed_check.wheel_speed_server:main',
            'client = wheel_speed_check.wheel_speed_client:main',
        ],
    },
)
