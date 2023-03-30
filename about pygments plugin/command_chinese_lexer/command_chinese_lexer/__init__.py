from pygments.lexer import RegexLexer
from pygments.token import *

__all__ = ['CustomLexer']

class CustomLexer(RegexLexer):
    name = 'Command_Chinese'
    aliases = ['command_chinese']
    filenames = ['*.txt']

    tokens = {
        'root': [
            
            # 随意 选 的种类
                # Keyword
                # Operator
                # Operator.Word
                # Literal.Number
            
            #(r"[◎○●☆★△▲□■▽▼◇◆]+", Keyword),
            (r"[◎○●☆★△▲∷□■▽▼◇◆·※]+", Keyword),
            (r"[↖↑↗←→↙↓↘⊙]+", Operator),
            (r"[Ａ-Ｚ]+", Operator.Word),
            (r"[①-⑩]+", Literal.Number),
            
            (r'.', Text),
        ]
    }