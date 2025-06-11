from setuptools import setup, find_packages

setup(
    name='cache_invalidator',
    version='0.1.0',
    description='A  pacakge for smart cache invalidation for Django applications',
    author='Thomas Pennant',
    author_email='pennqo@gmail.com',
    url='https://github.com/thomasx-0/cache_invalidator.git',
    packages=find_packages(),
    install_requires=[
        'Django>=3.0',
        'celery',  # Include if using Celery for task management
        # Add other dependencies as needed
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',  # Change as per your license
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)