from setuptools import setup, find_packages

setup(
    name='smart_cache_invalidator',
    version='0.1.0',
    description='A Django app for smart cache invalidation',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/smart_cache_invalidator',
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