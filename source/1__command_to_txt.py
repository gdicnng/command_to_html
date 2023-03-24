# -*- coding: utf_8_sig-*-
import os
import sys

file_in = r'command.dat'
file_out = r'command.txt'


# 切换工作目录
def change_working_directory():

    if getattr(sys, "frozen", False):
        # cx_Freeze 打包 忘了
        # pyinstall 打包 目录模式
        
        # The application is frozen
        executable_path = os.path.dirname(sys.executable)
        executable_path = os.path.abspath(executable_path)
        os.chdir( executable_path )
    else:
        # 以 python 脚本模式 运行
        
        # The application is not frozen
        # Change this bit to match where you store your data files:
        the_script_path = os.path.dirname(__file__)
        the_script_path = os.path.abspath(the_script_path)
        os.chdir( the_script_path )
change_working_directory()

replace_dict={
        # 参考  jjsnake 中文出招表，文件头
        # 参考补充 日文出扫表，文件头
        
        #   还需要再补充 mame 插件 data , button_char.lua 中的内容
        
        r"@A-button" : r"Ａ",
        r"@B-button" : r"Ｂ",
        r"@C-button" : r"Ｃ",
        r"@D-button" : r"Ｄ",
        r"@E-button" : r"Ｅ",
        r"@F-button" : r"Ｆ",
        r"@G-button" : r"Ｇ",
        r"@H-button" : r"Ｈ",
        r"@I-button" : r"Ｉ",
        r"@J-button" : r"Ｊ",
        r"@K-button" : r"Ｋ",
        r"@L-button" : r"Ｌ",
        r"@M-button" : r"Ｍ",
        r"@N-button" : r"Ｎ",
        r"@O-button" : r"Ｏ",
        r"@P-button" : r"Ｐ",
        r"@Q-button" : r"Ｑ",
        r"@R-button" : r"Ｒ",
        r"@S-button" : r"Ｓ",
        r"@T-button" : r"Ｔ",
        r"@U-button" : r"Ｕ",
        r"@V-button" : r"Ｖ",
        r"@W-button" : r"Ｗ",
        r"@X-button" : r"Ｘ",
        r"@Y-button" : r"Ｙ",
        r"@Z-button" : r"Ｚ", 
        
        r"^s"        : r"Ｓ", # Ｓ
        
        r"_A"        : r"Ａ",
        r"_B"        : r"Ｂ",
        r"_C"        : r"Ｃ",
        r"_D"        : r"Ｄ",
        
        r"_Z"        : r"Ｚ",

        r"_+"  : r"＋",#gb2312
        r"_."  : r"…",
        r"_1"  : r"↙",
        r"_2"  : r"↓",
        r"_3"  : r"↘",
        r"_4"  : r"←",
        r"_5"  : r"⊕", # gbk  ??? ############### ☉☉⊕⊕
        r"_6"  : r"→",
        r"_7"  : r"↖",
        r"_8"  : r"↑",
        r"_9"  : r"↗",
        r"_N"  : r"Ｎ", # # # # 
        
        r"@BALL"  : r"⊕",# gbk  ??? ☉☉⊕⊕
        
        r"_a" : r"①",# ① gb2312
        r"_b" : r"②",
        r"_c" : r"③",
        r"_d" : r"④",
        r"_e" : r"⑤",
        r"_f" : r"⑥",
        r"_g" : r"⑦",
        r"_h" : r"⑧",
        r"_i" : r"⑨",
        r"_j" : r"⑩",
        
        r"@decrease" : r"－",
        r"@increase" : r"＋",
        
        r"_S":r"开始键",
        r"^S":r"选择键",
        r"_P":r"拳",
        r"_K":r"脚",
        r"_G":r"防",
        r"^E":r"轻拳",
        r"^F":r"中拳",
        r"^G":r"重拳",
        r"^H":r"轻脚",
        r"^I":r"中脚",
        r"^J":r"重脚",
        r"^T":r"三脚同时输入",
        r"^U":r"三拳同时输入",
        r"^V":r"两脚同时输入",
        r"^W":r"两拳同时输入",
        
        r"@start"   : r"开始键",
        r"@select"  : r"选择键",
        r"@punch"   : r"拳",
        r"@kick"    : r"脚",
        r"@guard"   : r"防",
        r"@L-punch" : r"轻拳",
        r"@M-punch" : r"中拳",
        r"@S-punch" : r"重拳",
        r"@L-kick"  : r"轻脚",
        r"@M-kick"  : r"中脚",
        r"@S-kick"  : r"重脚",
        r"@3-kick"  : r"三脚同时输入",
        r"@3-punch" : r"三拳同时输入",
        r"@2-kick"  : r"两脚同时输入",
        r"@2-punch" : r"两拳同时输入",
        
        r"@custom1" : r"自定义①",# ① gb2312
        r"@custom2" : r"自定义②",
        r"@custom3" : r"自定义③",
        r"@custom4" : r"自定义④",
        r"@custom5" : r"自定义⑤",
        r"@custom6" : r"自定义⑥",
        r"@custom7" : r"自定义⑦",
        r"@custom8" : r"自定义⑧",
        r"@up"      : r"↑",
        r"@down"    : r"↓",
        r"@left"    : r"←",
        r"@right"   : r"→",
        r"@lever"   : r"Φ",# gb2312 ????? Φф
        r"@nplayer" : r"Pn", #
        r"@1player" : r"P1", #
        r"@2player" : r"P2", #
        r"@3player" : r"P3", #
        r"@4player" : r"P4", #
        r"@5player" : r"P5", #
        r"@6player" : r"P6", #
        r"@7player" : r"P7", #
        r"@8player" : r"P8", #
        
        r"_`" : r"・",#gb2312
        r"_@" : r"◎",#gb2312
        r"_)" : r"○",#gb2312
        r"_(" : r"●",#gb2312
        r"_*" : r"☆",#gb2312
        r"_&" : r"★",#gb2312
        r"_%" : r"△",#gb2312
        r"_$" : r"▲",#gb2312
        r"_#" : r"",       #gbk 里有 ，没有 ▣ ,▣ 25a3 ,回字 ？
        r"_]" : r"□",#gb2312
        r"_[" : r"■",#gb2312
        r"_{" : r"▽",       #gbk
        r"_}" : r"▼",       #gbk
        r"_<" : r"◇",#gb2312
        r"_>" : r"◆",#gb2312
        
        r"_|" : r"跳",
        r"_O" : r"按住", #?
        r"_-" : r"空中",
        r"_=" : r"下蹲",
        r"^-" : r"靠近",
        r"^=" : r"离开",
        r"_~" : r"蓄", #?
        r"^*" : r"连按", # Serious Tap ? # ボタン連打 ????  | ^* | @tap      |
        r"^?" : r"任意键",
        
        r"@jump"  : r"跳",
        r"@hold"  : r"按住", # # ??
        r"@air"   : r"空中",
        r"@sit"   : r"下蹲",
        r"@close" : r"靠近",
        r"@away"  : r"离开",
        r"@charge": r"蓄", # # ??
        r"@tap"   : r"连按",
        r"@button": r"任意键",
        
        r"_k" : r"→↘↓↙←", # ????? 这下面一大堆
        r"_l" : r"←↖↑↗→",
        r"_m" : r"←↙↓↘→",
        r"_n" : r"→↗↑↖←",
        r"_o" : r"→↘↓",
        r"_p" : r"↓↙←",
        r"_q" : r"←↖↑",
        r"_r" : r"↑↗→",
        r"_s" : r"←↙↓",
        r"_t" : r"↓↘→",
        r"_u" : r"→↗↑",
        r"_v" : r"↑↖←",
        r"_w" : r"从下开始顺时针一圈", # ??
        r"_x" : r"从上开始顺时针一圈", # ??
        r"_y" : r"从上开始逆时针一圈", # ??
        r"_z" : r"从下开始逆时针一圈", # ??
        r"_L" : r"→→",
        r"_M" : r"←←",
        r"_Q" : r"→↓↘",
        r"_R" : r"←↓↙",
        
        # → ← ↑ ↓↖ ↗ ↘ ↙ 
        r"@hcb" : r"→↘↓↙←",# half circle back
        r"@huf" : r"←↖↑↗→",
        r"@hcf" : r"←↙↓↘→", # half circle forward
        r"@hub" : r"→↗↑↖←",
        r"@qfd" : r"→↘↓",
        r"@qdb" : r"↓↙←",
        r"@qbu" : r"←↖↑",
        r"@quf" : r"↑↗→",
        r"@qbd" : r"←↙↓",
        r"@qdf" : r"↓↘→", # qcf ? quarter circle forward
        r"@qfu" : r"→↗↑",
        r"@qub" : r"↑↖←",
        r"@fdf" : r"从下开始顺时针一圈", # ??
        r"@fub" : r"从上开始顺时针一圈", # ??
        r"@fuf" : r"从上开始逆时针一圈", # ??
        r"@fdb" : r"从下开始逆时针一圈", # ??
        r"@xff" : r"→→",
        r"@xbb" : r"←←",
        r"@dsf" : r"→↓↘",
        r"@dsb" : r"←↓↙",

        r"_!" : r"→",
        r"^!" : r"└→",
        r"^1" : r"↙蓄",
        r"^2" : r"↓蓄",
        r"^3" : r"↘蓄",
        r"^4" : r"←蓄",
        r"^6" : r"→蓄",
        r"^7" : r"↖蓄",
        r"^8" : r"↑蓄",
        r"^9" : r"↗蓄",
        
        r"@-->" : r"→",
        r"@==>" : r"└→",
        
        # mame 插件 ,data,button_char.lua 补充
        r"@AIR" : r"空中",# @AIR
        r"@DIR" : r"DIR",# @DIR
        r"@MAX" : r"最大",# @MAX
        r"@TAP" : r"TAP",# @TAP ??????
        
        r"^M" : r"最大",# ^M   # MAX
        
        r"_?" : r"DIR",# _?
        r"_H" : r"Ｈ",# _H
        r"_X" : r"TAP",# _X ?????
        r"_^" : r"空中",# _^

        }

# 字符替换
def line_replace(line):
    
    for x in replace_dict: 
        line = line.replace(x,replace_dict[x])
    
    return line


with open(file_in,mode="rt",encoding="utf_8_sig",errors="backslashreplace") as f:
    content = f.readlines()

with open(file_out,mode="wt",encoding="utf_8_sig") as f_out:
    
    # 第一个 文件头 查找
    count = 0
    for line in content:
        count+=1
        line_string = line.strip()
        if line_string.startswith( r"$info" ):
            break
    
    # 文件头
    #   原始内容写入
    # if count > 0 :
    for line in content[:count]:
        f_out.write(line)
    
    # 后面的内容
    for line in content[count:]:
        
        line_string = line.strip()
        
        # 注释 行
        if line_string.startswith(r"#"):
            f_out.write(line)
        
        # 开始 标记 行
        elif line_string.startswith(r"$info"):
            f_out.write(line)
        
        # 正文
        else:
            line = line_replace(line)
            f_out.write(line)
