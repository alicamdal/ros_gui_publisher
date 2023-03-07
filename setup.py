from setuptools import setup

package_name = 'ros_gui'
camera_event = "ros_gui/CameraEvent"

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name, camera_event],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lent',
    maintainer_email='camdala@tcd.ie',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [    
            'streamer = ros_gui.streamer_function:main',
        ],
    },
)
