from pygments.lexer import RegexLexer
from pygments.token import *

__all__ = ['CustomLexer']

class CustomLexer(RegexLexer):
    name = 'Command_Chinese'
    aliases = ['command_chinese']
    filenames = ['*.txt']

    tokens = {
        'root': [
        
            (r"[◎○●☆★△▲□■▽▼◇◆]+", Generic.Error),
            (r"[↖↑↗←→↙↓↘⊕]+", Generic.Inserted),
            (r"[Ａ-Ｚ]+", Generic.Inserted),
            (r"[①-⑩]+", Generic.Inserted),
            (r"・", Generic.Inserted),
            #(r"·", Generic.Inserted),
            
            
            #(r"a", Generic.Inserted),
            #(r"A", Generic.Inserted),
            #(r'b', Generic.Inserted),
            #(r'c', Generic.Deleted),
            #(r'd', Generic.Subheading),
            #(r'e', Generic.Heading),
            #(r'f', Generic.Heading),
            (r'.', Text),
        ]
    }