from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),  # どのpackageディレクトリを含めるか伝える
    include_package_data=True,  # staticやtemplatesディレクトリのようなその他のファイルを含めるか
    zip_safe=False,
    install_requires=[
        'flask'
    ]
)
