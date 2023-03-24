import os
import sys
import re

# 文件夹 games
folder_name= "games"
# 文件
file_in = "command.txt"

file_out_header="header.txt"

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

# 创建文件夹
if os.path.isfile(folder_name):
    os.remove(folder_name)
if not os.path.isdir(folder_name):
    os.makedirs(folder_name)

# 文件内容
with open(file_in,mode="rt",encoding="utf_8_sig",errors="backslashreplace") as f:
    file_content = f.readlines()

# header
# 文件头，写入、清理
count = -1 # 从第0行开始
with open(file_out_header,mode="wt",encoding="utf_8_sig") as f_out:

    # 第一个 文件头 查找
    for line in file_content:
        count+=1
        line_string = line.strip()
        if line_string.startswith( r"$info" ):
            break
    
    # 第一项 前面 一般有 游戏名 注释
    if count > 0:
        if file_content[count-1].startswith("#"):# 检查 游戏名注释
            count -= 1

    if count > 0 :

        # 文件头， 写出到文本
        for line in file_content[:count] :
            f_out.write(line) 
    
        # 内容，清除 文件头
        file_content = file_content[count:]

# 找出内容开始所在的行
# 检查前一行是否为注释（一般为 游戏名注释）
game_info_start_line_number__set = set()
game_name_comment_line_number__set = set()
# 找出内容开始所在的行
count = 0
for line in file_content:
    line_string = line.strip()
    if line_string.startswith( r"$info" ):
        game_info_start_line_number__set.add(count)
    count+=1
# 检查前一行是否为注释（一般为 游戏名注释）
# 后面 没用 到 这个了
for line_number in game_info_start_line_number__set:
    if line_number > 0:
        title_line_number = line_number - 1
        if file_content[title_line_number].strip().startswith("#"):
            game_name_comment_line_number__set.add(title_line_number)

# with open("text_aaa.txt",mode="wt",encoding="utf_8_sig") as f:
#     for line in file_content:
#         f.write(line)



def command_format(content): # 此函数 从 JJui 复制

    if content is None:
        return None
    
    count = 0
    
    new_coutent={}
    # 以数量为 key
    # 从 1 开始
    # 把 0 留作 全部 用，
    # ttk.Combobox  .current()
    
    # 目录 全部 : 全部。
    
    # 目录 1 ： 内容 ，从这里开始
    # 目录 2 ： 内容
    # 目录 3 ： 内容
    # 目录 4 ： 内容
    # 目录 ……
    # {1:"lines",2:"lines",……}
    
    #$cmd
    #$end
    
    str_sart = r'^\s*\$cmd'
    str_end  = r'^\s*\$end'
    
    p_start  = re.compile(str_sart)
    p_end    = re.compile(str_end)
    
    flag = False
    
    for line in content:
        if flag:
        
            m_end = p_end.search(line) # 配匹 结束 标记
            
            if m_end:
                flag = False # 标记 取消
            else:
                if count in new_coutent:
                    new_coutent[count].append(line)
                else:
                    new_coutent[count]=[]  # 初始化
                    new_coutent[count].append(line)
            
        else:
            m_start = p_start.search(line) # 配匹 开始 标记
            if m_start:
                flag = True # 标记
                count += 1
                
    
    
    if len(new_coutent) == 0:
        return None
    else:
        return new_coutent
# 内容输出
#   游戏名.rst
#   子文件夹
#       每一个游戏一个文件夹，此处保留原始 文本
#       目录分层的话，需要多个文件，0000.txt - ????.txt ,utf_8
# 条件，没有，游戏名重复的
file_content_lines = len(file_content)
for number in sorted( game_info_start_line_number__set ):

    # 查找 title_string
    title_string = ""
    number_t = number
    while file_content[number_t - 1].strip().startswith("#"):
        number_t = number_t - 1
    if number_t != number:
        title_string = file_content[number_t].strip().lstrip("#")
    title_string_number = number_t
    
    game_info = []
    game_info.append(file_content[number])

    for n in range(number + 1,file_content_lines):
        line = file_content[n]
        if line.strip().startswith(r"$info"):
            break
        else:
            game_info.append(line)

    if game_info: # 去掉 下一个 游戏 ，的 游戏名 注释
        if game_info[-1].strip().startswith("#"):
            game_info=game_info[:-1]

    # $info= ，开始行
    first_game_name=""
    game_name_list = []
    start_line_string = file_content[number].strip().lower()
    start_line_string = start_line_string[6:] # $info=
    for game_name in  start_line_string.split( r"," ):
        game_name = game_name.strip().lower()
        if game_name:
            game_name_list.append(game_name)
    if game_name_list:
        first_game_name = game_name_list[0]

    if first_game_name:
        print()
        print(first_game_name)
        print(game_name_list)

        game_info_new = command_format(game_info)

        if game_info_new:

            game_info_folder = os.path.join(folder_name,first_game_name)
            if not os.path.isdir(game_info_folder):
                os.makedirs(game_info_folder)

            the_key_list = sorted(game_info_new.keys())

            # 写入 文本
            for the_key in the_key_list:
                file_name = os.path.join(game_info_folder,str(the_key) + ".txt")

                with open(file_name,mode="wt",encoding="utf_8") as f:
                    for line in game_info_new[the_key]:
                        f.write(line)

            # 生成，各游戏 .rst 文件
            for game_name in game_name_list:
                file_name = os.path.join(folder_name , game_name + ".rst")
                with open(file_name,mode="wt",encoding="utf_8") as f:
                    # =========
                    # title
                    # =========
                    # title_string
                    # new_title_string , 克隆版 游戏 缩写不同
                    new_title_string = game_name + " " + title_string
                    print("="*len(new_title_string)*3,file=f)
                    print(new_title_string,file=f)
                    print("="*len(new_title_string)*3,file=f)
                    print("",file=f)

                    # title_string ，可能不只一行
                    # info=
                    n=title_string_number
                    while(n<number):
                        print(file_content[n],file=f)
                        print("",file=f)
                        n += 1
                    #print(title_string,file=f)
                    print("",file=f)
                    print(file_content[number],file=f)
                    print("",file=f)
                    print("",file=f)

                    # 小标题
                    # ==========
                    for the_key in the_key_list:
                        title_2_string=str(the_key)
                        if game_info_new[the_key]:
                            if game_info_new[the_key][0]:
                                title_2_string = game_info_new[the_key][0].strip()
                        # 小标题
                        print(title_2_string,file=f)
                        print("="*len(title_2_string)*3,file=f)
                        print("",file=f)
                        # 引用内容
                        # .. literalinclude:: 1.txt
                        print(r".. literalinclude:: " + first_game_name + "/" + str(the_key) + ".txt" ,file=f)
                        print("",file=f)
