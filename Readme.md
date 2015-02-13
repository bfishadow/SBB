# SBB

**SBB**(**S**ina **B**log **B**ook) is a script to download all artcles from a specific [Sina Blog](http://blog.sina.com.cn/) blogger.

Based on these downloaded HTML files, you might generate an ebook by importing into [Calibre](http://calibre-ebook.com/). Or, you can simply save them anywhere as archives.

Tested with Python 2.7.8

### Usage
SBB.py (Sina Blog URL)

Example:

- SBB.py http://blog.sina.com.cn/gongmin
- SBB.py http://blog.sina.com.cn/u/1239657051

### Roadmap
- [ ] Add a datestamp for Index.html
- [ ] 'SELECT * FROM AllBlogPosts ORDER BY DatePosted DESC / ASC'
- [ ] Download the embed pictures
- [ ] Intergrate Calibre lib to generate eBook in one place

### License
Licensed under the Apache License, Version 2.0

#中文

**SBB**(**S**ina **B**log **B**ook) 是一个用于下载指定新浪博客作者全部文章的脚本。

基于这些下载来的 HTML 文件，您可以借助 [Calibre](http://calibre-ebook.com/) 来生成电子书，或者当作存档。

请在 Python 2.7.8 下使用。

### 用法
SBB.py <新浪博客地址>

例子：

- SBB.py http://blog.sina.com.cn/gongmin
- SBB.py http://blog.sina.com.cn/u/1239657051

### Roadmap
- [ ] 首页增加时间戳
- [ ] 'SELECT * FROM AllBlogPosts ORDER BY DatePosted DESC / ASC'
- [ ] 增加下载图片选项
- [ ] 整合 Calibre 库，一站式打包成 .mobi 或 .ePub

### 授权
Licensed under the Apache License, Version 2.0
