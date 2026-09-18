from setuptools import find_packages, setup

package_name = 'delivery_navigation'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (
            'share/' + package_name + '/launch',
            ['launch/navigation_launch.py']
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='aya_gebril',
    maintainer_email='aya2gebril@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'nav_publisher = delivery_navigation.nodes.nav_publisher:main',
            'nav_subscriber = delivery_navigation.nodes.nav_subscriber:main',
            'nav_service_server = delivery_navigation.nodes.nav_service_server:main',
        ],
    },
)
