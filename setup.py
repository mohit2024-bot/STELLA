from setuptools import setup,find_packages

setup(
    name= 'NetHyTech-STT',
    version='0.1',
    author='Mohit Kushwaha',
    author_email='example@gmail.com',
    description='this is speech to text package created by Mohit Kushwaha'
    
)
packages = find_packages(),
install_requirement = [
    'selenium',
    'webdriver_manager',
    
]
