#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '0.01'
__author__ = 'Julien G. (@bfishadow)'

'''
This script will download all artcles from a specific Sina Blog.
You might generate an ebook based on these HTML files.
Or simply save them as archives.
'''

import urllib2

def getBetween(str, str1, str2):
  strOutput = str[str.find(str1)+len(str1):str.find(str2)]
  return strOutput

def getArticle(strURL):

'''
"<!-- 正文开始 -->"
"<!-- 正文结束 -->"
<link href="http://simg.sinajs.cn/blog7style/css/conf/blog/article.css" type="text/css" rel="stylesheet" />

'''

  return

strTargetUID = "2488313871"

#first Load: get list for first page and article count
strTargetBlogURL = "http://blog.sina.com.cn/s/articlelist_" + strTargetUID + "_0_1.html"

'''
List URL Scheme -> http://blog.sina.com.cn/s/articlelist_[UID]_[Category ID]_[Page Number].html
e.g.
http://blog.sina.com.cn/s/articlelist_2488313871_0_2.html
http://blog.sina.com.cn/s/articlelist_2488313871_0_3.html
'''

objResponse = urllib2.urlopen(strTargetBlogURL)
strResponse = objResponse.read()
objResponse.close()

strBlogPostList = getBetween(getBetween(strResponse,"$blogArticleSortArticleids","$blogArticleCategoryids"), " : [", "],")

strBlogPostID = strBlogPostList

strBlogPageCount = getBetween(getBetween(strResponse, "全部博文", "<!--第一列end-->"),"<em>(", ")</em>")
intBlogPostCount = int(strBlogPageCount)  #article count
intPageCount = int(intBlogPostCount/50)+1 #page count, default page size is 50

#Second load: get list for the rest of pages
for intCurrentPage in range(intPageCount - 1) :
  strTargetBlogURL = "http://blog.sina.com.cn/s/articlelist_" + strTargetUID + "_0_" + str(intCurrentPage + 2) + ".html"
  objResponse = urllib2.urlopen(strTargetBlogURL)
  strResponse = objResponse.read()
  strBlogPostList = getBetween(getBetween(strResponse,"$blogArticleSortArticleids","$blogArticleCategoryids"), " : [", "],")
  strBlogPostID = strBlogPostID + "," + strBlogPostList
  objResponse.close()

strBlogPostID = strBlogPostID.replace('"','')
#strBlogPostID <- this string has all article IDs for current blog


#Third load: get all articles one by one

'''
Blog page URL Scheme -> http://blog.sina.com.cn/s/blog_[Article ID].html
'''

arrBlogPost = strBlogPostID.split(',')
intCounter = 0
for strCurrentBlogPostID in arrBlogPost :
  intCounter = intCounter + 1
  print intCounter, "http://blog.sina.com.cn/s/blog_" + strCurrentBlogPostID + ".html"

strTargetBlogPostURL = "http://blog.sina.com.cn/main_v5/ria/print.html?blog_id=blog_9450a80f0102vbwd"








