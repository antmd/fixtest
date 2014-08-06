from setuptools import setup, find_packages

setup(
	name='fixtest',
	version='0.1',
	packages=find_packages(),
	install_requires=['twisted>=14.0.0'],
	license='MIT',
	author='Kenn Takara',
	entry_points={
		'console_scripts': ['fixtest=fixtest.base.runner:main'],
	},
	classifiers={
		'Development Status :: 2 - Pre-Alpha',
		'Intended Audience :: Developers',
		'Intended Audience :: Financial and Insurance Industry',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 2.7',
		'Topic :: System :: Networking',
		'Topic :: Software Development :: Testing',
	},
	url='https://github.com/kennt/fixtest'
)