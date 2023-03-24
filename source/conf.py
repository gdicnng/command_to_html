# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


import sys
import os
print(sys.path)

the_script_path = os.path.dirname(__file__)
print(the_script_path)

sys.path.append(the_script_path)
print(the_script_path)


# 自定义 lexer
import command_chinese_lexer

# https://py-generic-project.readthedocs.io/en/latest/authoring.html#adding-a-custom-pygments-lexer-to-sphinx
# In order for Sphinx to load and recognize a custom lexer, two things are needed:
# 
#         1 Add the package name of the lexer to the extensions list in conf.py. Of course, that package has to be importable, either by using a virtualenv or manipulating sys.path.
#         2 Give your lexer package a Setuptools pygments.lexers entry point.
#               ？？？？？
# 
# Then use it in a code-block as if it were a built-in. That’s all.
#
# https://github.com/pygments/pygments/issues/1096#issuecomment-1426809706
# I am using the following hack somewhere in my code:
#LEXERS["PigeonLexer"] = ("extensions.pygments", "Pigeon", ("pigeon",), (), ())
from pygments.lexers import LEXERS
#print(type(LEXERS)) 
#print(LEXERS)
LEXERS["CustomLexer"] = ("command_chinese_lexer", "Command_Chinese", ("command_chinese",), (), ())

print()
print()

########################
########################
########################
########################
project = 'command_html'
copyright = '2023, gdicnng'
author = 'gdicnng'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']


#######################
#######################
#######################
#######################

html_theme = 'alabaster'
#html_theme = 'sphinx_rtd_theme'
#html_theme = 'python_docs_theme'
#html_theme = 'classic'
#html_theme = 'sphinxdoc'
# alabaster classic sphinx_rtd_theme

# python 2 classic
# python 3 theme
# python_docs_theme
#   https://sphinx-themes.org/sample-sites/python-docs-theme/
#   pip install python-docs-theme

# sphinx_rtd_theme
#   $ pip install sphinx-rtd-theme

###'<project> v<revision> documentation'
html_title = ''
# 此值为空时，python 3 docs 顶部 少一节
# 此值不为这 每个网页标题后缀
##
# 设置为空
# 默认值： '<project> v<revision> documentation'
# The “title” for HTML documentation generated with Sphinx’s own templates. This is appended to the <title> tag of individual pages, and used in the navigation bar as the “topmost” element. It defaults to '<project> v<revision> documentation'.



######
######
######
# 自己添加
#自己添加 1
if html_theme == 'alabaster':
    html_theme_options = {
        # https://www.sphinx-doc.org/en/master/usage/theming.html#builtin-themes
        # https://alabaster.readthedocs.io/en/latest/customization.html
        
        # description: Text blurb about your project, to appear under the logo.
        #'description':"gdicnng",
        
        # 'logo': 'logo.png',
        #'logo': 'logo.png',
        
        'caption_font_family' : 'SimHei,KaiTi,NSimSun,SimSun',# alabaster theme
        
        #'code_font_family': 'NSimSun,SimSun,SimHei,KaiTi',# alabaster theme
        'code_font_family': 'NSimSun,SimSun,KaiTi,SimHei',# alabaster theme
        
        'font_family' : 'NSimSun,SimSun,SimHei,KaiTi',# alabaster theme
        
        'head_font_family' : 'SimHei,KaiTi,NSimSun,SimSun',# alabaster theme
        
        'show_relbars' : 'true',# alabaster theme
        'show_powered_by': 'true',# alabaster theme
        'fixed_sidebar' : 'false',# alabaster theme，目录条不同主体内容一起上下滚动
        'body_max_width' : 'none',# 主体内容宽度不限，basic theme
        'page_width' : 'none' ,# 主体内容宽度不限，alabaster theme
        'globaltoc_maxdepth' : -1 ,# basic theme
    #    'nosidebar' : 'true',# basic theme
        'sidebar_collapse':'true',# alabaster theme
        'globaltoc_collapse':'true',# basic
    }
elif html_theme == 'classic': # python 2
    # python doc 2
    html_theme_options ={
        'body_max_width' : 'none',# 主体内容宽度不限，basic theme
        'globaltoc_collapse' : 'true',# basic theme 
            # Only expand subsections of the current document in globaltoc.html
        'globaltoc_maxdepth' : '-1',# basic theme
        'bodyfont':'NSimSun,SimSun,SimHei,KaiTi',# basic
        'headfont':'SimHei,KaiTi,NSimSun,SimSun',# basic
    }
elif html_theme == "python_docs_theme": # python 3
    # python doc 3
    # pip install python-docs-theme
    
    #'<project> v<revision> documentation'
    html_title = project
    #html_title = ""
    # 每一个页面 后缀，如果不为空，感觉烦人
    # 如果 设为空 ，
        # 此 主题 顶部 目录  a >> b >> c >> ..... ，
        # b 处，显示空白
    
    # inherit = default
    # inherit = classic
    # inherit = basic
    html_theme_options ={
        'body_max_width' : 'none',# 主体内容宽度不限，basic theme
        'globaltoc_collapse':'true',# basic,
        'globaltoc_maxdepth' : '-1',# basic theme
        'root_name' : 'JJui',
        'root_url' : '/index.html', # 空的，无效
        'root_icon':'', 
        'root_include_title':True, 
            # a >> b >> c >> ..... ， 头部目录，显示/不显示 b
            # 头部 第一个 a ，删不掉

    }
elif html_theme == 'sphinx_rtd_theme':# inherit  basic
    html_static_path = ['_static_rtd',]
    html_css_files = ['custom.css',]
        # 添加 custom.css ，改变宽度
    html_theme_options ={
        # 页面宽度 怎样 不限制 ？
        'collapse_navigation':True,
        'bodyfont':'KaiTi,SimSun,NSimSun,SimHei',# basic
        #'headfont':'SimHei,KaiTi,NSimSun,SimSun',# basic        
    }
# SimSun 宋体
# SimHei 黑体
# NSimSun 新宋体
# Microsoft Yahei 微软雅黑
# KaiTi 楷体
# Microsoft JhengHei 微软正黑体

#   'globaltoc_maxdepth' : 1 ,
# html_sidebars 上 globaltoc.html 目录深度
# 1 2 3 ...
# sidebar 太长时，没有 拖拽 栏

# ###
# show_powered_by
# show_relbars: true or false - used to display next and previous links above and below the main page content. If you only want to display one, this setting can be further overridden through the show_relbar_top and show_relbar_bottom settings.



# 自己添加 3
# 关闭高亮
#highlight_language = 'none'
highlight_language = 'command_chinese' # 自定义
pygments_style = 'default'
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-pygments_style

# 复制源代码 到 build/html
html_copy_source = False
# 显示源代码 按钮
#html_show_sourcelink = False
html_show_sourcelink = False


html_show_copyright = True
# If true, “(C) Copyright …” is shown in the HTML footer. Default is True.
html_show_sphinx = True
# If true, “Created using Sphinx” is shown in the HTML footer. Default is True.
# 受 alabaster theme 影响：  'show_powered_by': 'true',# alabaster theme

html_output_encoding = 'utf-8'
# 默认值 'utf-8'
# Encoding of HTML output files. Default is 'utf-8'. Note that this encoding name must both be a valid Python encoding name and a valid HTML charset value.

# If true, “Created using Sphinx” is shown in the HTML footer. Default is True.
# ?????? 无效？theme alabaster 'show_powered_by' : 'false',
# html_show_sphinx = False



#import jieba
html_search_language = 'zh'

#r'c:\Users\x.j\AppData\Local\Programs\Python\Python38\Lib\site-packages\jieba\dict.txt'} 

# https://github.com/sphinx-doc/sphinx/issues/2169
# to enable chinese search
#html_search_language = 'zh'
# if you want to use custom jieba dictonary path.
# if not set , it use jieba dictonary in default
#html_search_options = {'dict': jieba.DEFAULT_DICT}
#html_search_options = {'dict': '/home/my/my_dictonary.txt'} 
############################################
## pip install jieba
try:
    import jieba
    html_search_options = {'dict': jieba.DEFAULT_DICT}
except:
    pass


#测试
html_sidebars = {
   '**': ['localtoc.html','searchbox.html'],#'searchbox.html'
   #'**': ['globaltoc.html', 'searchbox.html'],
   #localtoc.html – a fine-grained table of contents of the current document
   #globaltoc.html – a coarse-grained table of contents for the whole documentation set, collapsed
   #relations.html – two links to the previous and next documents
   #sourcelink.html – a link to the source of the current document, if enabled in html_show_sourcelink
   #searchbox.html – the “quick search” box
   'using/windows': ['windowssidebar.html',],
   #'using/windows': ['windowssidebar.html', 'searchbox.html'],
}


#
#extensions = ['recommonmark'] # for .md
source_suffix = {
    '.rst': 'restructuredtext',
    #'.md': 'markdown',
}


# If false, no module index is generated.
html_domain_indices = True

# If false, no index is generated.
html_use_index = False
# 不要 索引 
# 不要 顶部 索引 超链接，看着烦人