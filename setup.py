import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="yuzhuhwq5public", # 这里填写package名字
    version="0.0.1",
    author="Yuzhu Wang", # 这里填写你的名字
    author_email="15151843600@163.com", # 填写你的邮箱
    description="A bubbler sort package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/e0431421/bubblewangyuzhu", #这里填写github仓库的地址
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
