import sys
import os
print(sys.path)

the_script_path = os.path.dirname(__file__)
the_script_path = os.path.abspath(the_script_path)

sys.path.append(the_script_path)

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

########################
########################

project = '出招表'
copyright = '2023, gdicnng'
author = 'gdicnng'
release = '1.0'

extensions = []

templates_path = ['_templates']

exclude_patterns = []

language = 'zh_CN'


html_theme = 'alabaster'
html_static_path = ['_static']

###'<project> v<revision> documentation'
html_title = ''
# 设置为空


if html_theme == 'alabaster':
    html_theme_options = {
        # https://www.sphinx-doc.org/en/master/usage/theming.html#builtin-themes
        # https://alabaster.readthedocs.io/en/latest/customization.html
        
        # description: Text blurb about your project, to appear under the logo.
        #'description':"test",
        
        #'logo': 'logo.png',
        #"description":"text for logo",
        "logo_name":True,
        
        # SimSun 宋体
        # SimHei 黑体
        # NSimSun 新宋体
        # KaiTi 楷体
        
        'caption_font_family' : 'NSimSun,SimSun,SimHei,KaiTi', # alabaster theme
        #caption_font_size
        'caption_font_size': '50px',
        
        'code_font_family': 'NSimSun,SimSun,SimHei,KaiTi,monospace',# alabaster theme
        #'code_font_size':"1em", # em ,px
        
        'font_family' : 'NSimSun,SimSun,SimHei,KaiTi',# alabaster theme
        #'font_size':'20px',
        
        'head_font_family' : 'NSimSun,SimSun,SimHei,KaiTi',# alabaster theme
        
        'show_relbars' : True,# alabaster theme
        'show_powered_by': 'true',# alabaster theme
        'fixed_sidebar' : 'false',# alabaster theme，目录条不同主体内容一起上下滚动
        'body_max_width' : 'none',# 主体内容宽度不限，basic theme
        'page_width' : 'none' ,# 主体内容宽度不限，alabaster theme
        #'sidebar_width':'400px',
        'globaltoc_maxdepth' : -1 ,# basic theme
        #'nosidebar' : 'true',# basic theme
        'sidebar_collapse':'true',# alabaster theme
        'globaltoc_collapse':'true',# basic
        
        
    }





#highlight_language = 'none'
highlight_language = 'command_chinese' # 自定义
pygments_style = 'default'
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-pygments_style


html_copy_source = False
html_show_sourcelink = False

html_show_copyright = False
html_show_sphinx = True


html_output_encoding = 'utf-8'
# 默认值 'utf-8'
# Encoding of HTML output files. Default is 'utf-8'. Note that this encoding name must both be a valid Python encoding name and a valid HTML charset value.


html_search_language = 'zh'
## pip install jieba
try:
    import jieba
    html_search_options = {'dict': jieba.DEFAULT_DICT}
except:
    pass


#测试
html_sidebars = {
   '**': ['about.html','searchbox.html','localtoc.html',],
   'using/windows': ['windowssidebar.html',],
}


#extensions = ['recommonmark'] # for .md
source_suffix = {
    '.rst': 'restructuredtext',
    #'.md': 'markdown',
}


# If false, no module index is generated.
html_domain_indices = False

# If false, no index is generated.
html_use_index = False
# 不要 索引 
# 不要 顶部 索引 超链接，看着烦人


# html_scaled_image_link = False

# rst_epilog = ""
