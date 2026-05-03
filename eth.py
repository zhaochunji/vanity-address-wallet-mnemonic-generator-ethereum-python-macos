# ==============================================================================
# ============================ 全局可配置参数（完整版） ============================
# ==============================================================================
# ===【作者网站：https://github.com/zhaochunji】==================================
# ===【联系作者：zcjweb@gmail.com】===============================================
# ------------------------------ 【核心保留参数】 ------------------------------
ETH_ALPHA_CASE_SENSITIVE = True       # 字母检测是否区分大小写（True=区分，False=不区分）
ETH_ADDR_OUTPUT_CASE = "original"      # 导出地址大小写（original=原大小写，upper=全大写，lower=全小写）

# ------------------------------ 【顺子检测开关（核心）】 ------------------------------
ETH_SEQ_0_9_ENABLE = False              # 0~9正顺检测（纯数字，0123456789循环）
ETH_SEQ_0_9_MIN_LEN = 9               # 0~9正顺最小位数
ETH_SEQ_0_10_ENABLE = False              # 0~10正顺检测（纯数字，01234567891011...）
ETH_SEQ_0_10_MIN_LEN = 9              # 0~10正顺最小位数
ETH_REV_SEQ_0_9_ENABLE = False           # 0~9倒顺检测（纯数字，9876543210循环）
ETH_REV_SEQ_0_9_MIN_LEN = 9           # 0~9倒顺最小位数
ETH_REV_SEQ_0_10_ENABLE = False          # 0~10倒顺检测（纯数字，131211109876...）
ETH_REV_SEQ_0_10_MIN_LEN = 9          # 0~10倒顺最小位数

# ------------------------------ 【基础检测阈值】 ------------------------------
ETH_START_DIGIT_SAME = 9    # 开头连续相同数字阈值
ETH_START_ALPHA_SAME = 9    # 开头连续相同字母阈值
ETH_END_DIGIT_SAME = 9      # 结尾连续相同数字阈值
ETH_END_ALPHA_SAME = 9      # 结尾连续相同字母阈值
ETH_MID_DIGIT_SAME = 11     # 中间连续相同数字阈值
ETH_MID_ALPHA_SAME = 11     # 中间连续相同字母阈值

# ------------------------------ 【1位字符重复检测】 ------------------------------
ETH_1CHAR_REPEAT_MUST_CONTINUOUS = False # 单字符重复是否要求连续
ETH_1DIGIT_REPEAT_CHECK = True; ETH_1DIGIT_REPEAT_MIN = 19 # 单数字重复检测+阈值
ETH_1ALPHA_REPEAT_CHECK = True; ETH_1ALPHA_REPEAT_MIN = 19 # 单字母重复检测+阈值

# ------------------------------ 【2-10位数字/字母重复检测】 ------------------------------
ETH_REPEAT_MUST_CONTINUOUS = True      # 重复检测是否要求子串连续
# 数字重复（2-10位）
ETH_2DIGIT_REPEAT_CHECK = True; ETH_2DIGIT_REPEAT_MIN = 6
ETH_3DIGIT_REPEAT_CHECK = True; ETH_3DIGIT_REPEAT_MIN = 5
ETH_4DIGIT_REPEAT_CHECK = True; ETH_4DIGIT_REPEAT_MIN = 4
ETH_5DIGIT_REPEAT_CHECK = True; ETH_5DIGIT_REPEAT_MIN = 4
ETH_6DIGIT_REPEAT_CHECK = False; ETH_6DIGIT_REPEAT_MIN = 3
ETH_7DIGIT_REPEAT_CHECK = False; ETH_7DIGIT_REPEAT_MIN = 2
ETH_8DIGIT_REPEAT_CHECK = False; ETH_8DIGIT_REPEAT_MIN = 2
ETH_9DIGIT_REPEAT_CHECK = False; ETH_9DIGIT_REPEAT_MIN = 2
ETH_10DIGIT_REPEAT_CHECK = False; ETH_10DIGIT_REPEAT_MIN = 2
# 字母重复（2-10位）
ETH_2ALPHA_REPEAT_CHECK = True; ETH_2ALPHA_REPEAT_MIN = 6
ETH_3ALPHA_REPEAT_CHECK = True; ETH_3ALPHA_REPEAT_MIN = 5
ETH_4ALPHA_REPEAT_CHECK = True; ETH_4ALPHA_REPEAT_MIN = 4
ETH_5ALPHA_REPEAT_CHECK = True; ETH_5ALPHA_REPEAT_MIN = 4
ETH_6ALPHA_REPEAT_CHECK = False; ETH_6ALPHA_REPEAT_MIN = 3
ETH_7ALPHA_REPEAT_CHECK = False; ETH_7ALPHA_REPEAT_MIN = 2
ETH_8ALPHA_REPEAT_CHECK = False; ETH_8ALPHA_REPEAT_MIN = 2
ETH_9ALPHA_REPEAT_CHECK = False; ETH_9ALPHA_REPEAT_MIN = 2
ETH_10ALPHA_REPEAT_CHECK = False; ETH_10ALPHA_REPEAT_MIN = 2

# ------------------------------ 【自定义字符串检测】 ------------------------------
ETH_CUSTOM_STR_ENABLE = True      # 是否开启自定义字符串检测
ETH_CUSTOM_STR = "{8888888;88888888;888888888;999999999;99999999;00000000;88889999;77778888;123456789;12345678910;12345678;99995555;66778899;666777888;33333333;55555555;66666666;77777777;00000000;000000000;ABCDEF123456;ABCDEF123;123ABCDEF;ABCABCABC;EEEEEEEE;FFFFFFFF;DDDDDDDD;CCCCCCCC;BBBBBBBB;AAAAAAAA;aaaaaaaa;bbbbbbbb;cccccccc;dddddddd;eeeeeeee;ffffffff;80808080;8080808080;9999988888;98989898;39393939;38383838;123123123;11123456789;1112345678;AABBCCDD;A8A8A8A8;A9A9A9A9;ABC88888888;ABC888888;ABC8888888;988988988;99887766;00AABBCCDD;00ABCDABCD;88ABCDABCD;0088889999;0099998888;0066778899;0012341234;AA12341234;AA56785678;BaBa8888;BABA8888;CD88889999;CD77778888;CF55556666;AA88889999;AA77778888;AA88888888;AA99998888;2008080808;88088088088;33990000;ABCDEF;99998888;9999988888;9090909090;8080808080808080;880880880880;8888088880;98989898098;989898980;A88888888;A99999999;A999999999;A7777777;A66666666;ABC88888888;ABC8888888;ABC99999999;ABC999999999;A88B88C88D88E88F88;8888ABCD;8888abcd;8888BBBB;8B8B8B8B;B8B8B8B8;C9C9C9C9;AA00001111;AA11110000;11110000;1010101010;0101010101;BB88889999;BB9998888;CC88889999;CC99998888;AE88888888;AE98989898;AA12345678;AA66778899;AA55667788;AA23456789;A812345678;A912345678;A987654321;Ab66666666;AA88BB88BB;AABB88CC99;00ABCD5678;001234ABCD;00A1B1C1D1;00A8B8C8D8;00BBB8BBB8}"
ETH_CUSTOM_STR_CASE_SENSITIVE = True # 自定义字符串是否区分大小写
ETH_CUSTOM_STR_START_ENABLE = False  # 检测自定义字符串在地址开头
ETH_CUSTOM_STR_ANY_ENABLE = False    # 检测自定义字符串在地址任意位置
ETH_CUSTOM_STR_END_ENABLE = True    # 检测自定义字符串在地址结尾

# ------------------------------ 【其他基础检测开关】 ------------------------------
ETH_CHECK_FULL_NUM = True   # 检测纯数字地址
ETH_CHECK_FULL_ALPHA = True # 检测纯字母地址
ETH_CHECK_REPEAT_PATTERN = True # 检测重复模式（如121212）

# ------------------------------ 【字符包含/排除检测】 ------------------------------
ETH_EXCLUDE_CHARS_ENABLE = False         # 是否开启「不包含特定字符」检测
ETH_EXCLUDE_CHARS = "4"                 # 需要排除的字符
ETH_ONLY_ALLOW_CHARS_ENABLE = True      # 是否开启「仅包含特定字符」检测
ETH_ONLY_ALLOW_CHARS_LIST = ["01234", "5678", "67890", "89", "789", "6789", "36890", "890", "380", "390", "3890", "ABCDEF890", "ABCDEF6789", "A12345", "A7890", "ABCDEF89", "390ABC", "B8690", "ABCDE8", "ABCDE9", "ABCDE7", "ABC56789","ABC0123","AB8","ABCDEF8","A123"]  # 仅包含字符组合列表

# ------------------------------ 【前10位规则配置（0x后1-10位）】 ------------------------------
ETH_FIRST10_ENABLE = False # 前10位规则总开关
ETH_FIRST2_ENABLE = True; ETH_FIRST2_POOL = ["AA", "BB", "CC", "DD", "EE", "FF", "00", "11", "88", "99", "77", "66", "55", "33", "22", "A8", "A9", "B8", "0A", "0B", "01", "08", "09", "06", "12"] # 前2位检测开关+字符池
ETH_FIRST2_CASE_SENSITIVE = True # 前2位是否区分大小写
ETH_FIRST3_10_ENABLE = False # 第3-10位检测开关
# 3-10位子规则
ETH_FIRST3_10_BOMB_ENABLE = True; ETH_FIRST3_10_BOMB_POOL = ["00009999", "88889999", "77778888", "BBBBCCCC", "CCCCDDDD", "00008888", "00001111", "00002222", "00003333", "99998888", "33339999", "55556666", "66668888", "AAAABBBB", "AAAACCCC", "AAAADDDD", "AAAAEEEE", "AAAAFFFF", "BBBBAAAA", "BBBBBBBB", "BBBBCCCC", "AAAAAAAA", "BBBBDDDD", "BBBBEEEE", "BBBBFFFF", "CCCCAAAA", "CCCCBBBB", "CCCCCCCC", "CCCCDDDD", "CCCCEEEE", "CCCCFFFF", "DDDDAAAA", "DDDDBBBB", "DDDDCCCC", "DDDDDDDD", "DDDDEEEE", "DDDDFFFF", "EEEEAAAA", "EEEEBBBB", "EEEECCCC", "EEEEDDDD", "EEEEEEEE", "EEEEFFFF", "FFFFAAAA", "FFFFBBBB", "FFFFCCCC", "FFFFDDDD", "FFFFEEEE", "FFFFFFFF", "00005555", "00006666", "00007777", "00008888", "00009999", "00000000", "11110000", "11111111", "11112222", "11113333", "11115555", "11116666", "11117777", "11118888", "11119999", "22220000", "22222222", "22221111", "22223333", "22225555", "22226666", "22227777", "22228888", "22229999", "33330000", "33338888", "33339999", "33333333", "33336666", "66660000", "66666666", "66667777", "66668888", "66669999", "77770000", "88886666", "88880000", "88887777", "88888889", "66666789", "33333456", "11111234", "22222345", "89898989", "98989898", "99889988", "98899889", "08080808", "80808080", "90909090", "09090909", "ddddbbbb", "bbbbdddd", "bdbdbdbd", "dbdbdbdb", "AaAaAaAa", "aAaAaAaA", "AAAAaaaa", "aaaaAAAA", "aaaabbbb", "bbbbaaaa", "babababa", "abababab", "abcdABCD", "ABCDabcd", "ABCDDCBA", "abcddcba", "19491001", "19971997", "20082008", "88999988", "365D365D", "20482048", "10241024", "88488848", "88448844", "88668866", "86868686", "69696969", "66996699", "96969696", "68996899", "19491949", "00000001", "99999991", "99999888", "88899999"] # 双炸弹检测开关+池子
ETH_FIRST3_10_BOMB_CASE_SENSITIVE = True # 双炸弹是否区分大小写
ETH_FIRST3_10_SEQ_ENABLE = True; ETH_FIRST3_10_SEQ_POOL = ["12345678", "23456789", "98765432", "87654321"] # 顺子检测开关+池子
ETH_FIRST3_10_SEQ_CASE_SENSITIVE = True # 顺子是否区分大小写
ETH_FIRST3_10_DOUBLE_CHAR_ENABLE = True; ETH_FIRST3_10_DOUBLE_CHAR_POOL = ["22334455", "33445566", "44556677", "AABBCCDD", "BBCCDDEE", "CCDDEEFF", "AA88AA88", "AA88BB99", "66778899", "55667788", "11223344", "99887766", "CCDDBBAA", "AA88EE88", "AA88BB88", "88BB88BB", "8B8B8B8B", "88BB8899"] # 双字符检测开关+池子
ETH_FIRST3_10_DOUBLE_CHAR_CASE_SENSITIVE = True # 双字符是否区分大小写
ETH_FIRST3_10_PALINDROME_ENABLE = True; ETH_FIRST3_10_PALINDROME_POOL = ["12344321", "12211221", "ABCCBAAB", "80088008", "88999988", "67899876", "87655678", "98766789", "08800880", "98899889", "77877877", "88999988"] # 回文检测开关+池子
ETH_FIRST3_10_PALINDROME_CASE_SENSITIVE = True # 回文是否区分大小写

# ------------------------------ 【末尾10位规则配置（地址最后10位）】 ------------------------------
ETH_LAST10_ENABLE = True # 末尾10位规则总开关
ETH_LAST2_ENABLE = True; ETH_LAST2_POOL = ["AA", "BB", "CC", "DD", "EE", "FF", "66", "88", "99", "77", "22", "33", "11", "55", "00"] # 最后2位检测开关+字符池
ETH_LAST2_CASE_SENSITIVE = True # 最后2位是否区分大小写
ETH_LAST3_10_ENABLE = True # 倒数3-10位检测开关
# 倒数3-10位子规则
ETH_LAST3_10_BOMB_ENABLE = True; ETH_LAST3_10_BOMB_POOL = ETH_FIRST3_10_BOMB_POOL # 双炸弹检测开关+池子（复用前10位池子）
ETH_LAST3_10_BOMB_CASE_SENSITIVE = True # 双炸弹是否区分大小写
ETH_LAST3_10_SEQ_ENABLE = True; ETH_LAST3_10_SEQ_POOL = ETH_FIRST3_10_SEQ_POOL # 顺子检测开关+池子（复用）
ETH_LAST3_10_SEQ_CASE_SENSITIVE = True # 顺子是否区分大小写
ETH_LAST3_10_DOUBLE_CHAR_ENABLE = True; ETH_LAST3_10_DOUBLE_CHAR_POOL = ETH_FIRST3_10_DOUBLE_CHAR_POOL # 双字符检测开关+池子（复用）
ETH_LAST3_10_DOUBLE_CHAR_CASE_SENSITIVE = True # 双字符是否区分大小写
ETH_LAST3_10_PALINDROME_ENABLE = True; ETH_LAST3_10_PALINDROME_POOL = ETH_FIRST3_10_PALINDROME_POOL # 回文检测开关+池子（复用）
ETH_LAST3_10_PALINDROME_CASE_SENSITIVE = True # 回文是否区分大小写

# ------------------------------ 【40位精细化字符规则配置】 ------------------------------
ETH_40CHAR_RULE_ENABLE = False  # 40位字符规则总开关
ETH_40CHAR_SEGMENTS = [
    (1, 1, "ABCDEFabcdef1234567890", True, None),
    (2, 2, "ABCDEFabcdef1234567890", True, None),
    (3, 3, "ABCDEFabcdef1234567890", True, None),
    (4, 4, "ABCDEFabcdef1234567890", True, None),
    (5, 5, "ABCDEFabcdef1234567890", True, None),
    (6, 6, "ABCDEFabcdef1234567890", True, None),
    (7, 7, "ABCDEFabcdef1234567890", True, None),
    (8, 8, "ABCDEFabcdef1234567890", True, None),
    (9, 9, "ABCDEFabcdef1234567890", True, None),
    (10, 10, "ABCDEFabcdef1234567890", True, None),
    (11, 11, "AABCDEFabcdef1234567890", True, None),
    (12, 12, "ABCDEFabcdef1234567890", True, None),
    (13, 13, "ABCDEFabcdef1234567890", True, None),
    (14, 14, "ABCDEFabcdef1234567890", True, None),
    (15, 15, "ABCDEFabcdef1234567890", True, None),
    (16, 16, "ABCDEFabcdef1234567890", True, None),
    (17, 17, "ABCDEFabcdef1234567890", True, None),
    (18, 18, "ABCDEFabcdef1234567890", True, None),
    (19, 19, "ABCDEFabcdef1234567890", True, None),
    (20, 20, "ABCDEFabcdef1234567890", True, None),
    (21, 21, "ABCDEFabcdef1234567890", True, None),
    (22, 22, "ABCDEFabcdef1234567890", True, None),
    (23, 23, "ABCDEFabcdef1234567890", True, None),
    (24, 24, "ABCDEFabcdef1234567890", True, None),
    (25, 25, "ABCDEFabcdef1234567890", True, None),
    (26, 26, "ABCDEFabcdef1234567890", True, None),
    (27, 27, "ABCDEFabcdef1234567890", True, None),
    (28, 28, "ABCDEFabcdef1234567890", True, None),
    (29, 29, "ABCDEFabcdef1234567890", True, None),
    (30, 30, "ABCDEFabcdef1234567890", True, None),
    (31, 31, "ABCDEFabcdef1234567890", True, None),
    (32, 32, "ABCDEFabcdef1234567890", True, None),
    (33, 33, "ABCDEFabcdef1234567890", True, None),
    (34, 34, "ABCDEFabcdef1234567890", True, None),
    (35, 35, "ABCDEFabcdef1234567890", True, None),
    (36, 36, "ABCDEFabcdef1234567890", True, None),
    (37, 37, "ABCDEFabcdef1234567890", True, None),
    (38, 38, "ABCDEFabcdef1234567890", True, None),
    (39, 39, "ABCDEFabcdef1234567890", True, None),
    (40, 40, "ABCDEFabcdef1234567890", True, None),
]

# ==============================================================================
# ==================== 【前缀 / 后缀 重复模式（带详细注释）】 ====================
# ==============================================================================
# 【总开关】：是否启用整个前缀/后缀重复搜索功能
ETH_PREFIX_SUFFIX_REPEAT_ENABLE = True

# -------------------------- 前缀重复（0x 后面开头部分） --------------------------
# 例子：0x123123123123 = 前缀3位重复4次
ETH_PREFIX_REPEAT_ENABLE = True  # 前缀重复总开关

# 前缀：1~10位 单元是否开启
# 索引 0=1位, 1=2位, 2=3位, 3=4位, 4=5位, 5=6位, 6=7位, 7=8位, 8=9位,9=10位
ETH_PREFIX_LEN_ENABLE = [
    False,   # 0: 1位前缀  如 88888
    True,   # 1: 2位前缀  如 121212
    True,   # 2: 3位前缀  如 123123123
    True,   # 3: 4位前缀
    True,   # 4: 5位前缀
    True,   # 5: 6位前缀
    True,   # 6: 7位前缀
    True,   # 7: 8位前缀
    True,   # 8: 9位前缀
    True,   # 9:10位前缀
]

# 前缀：每种长度允许的重复次数（2~10次）
# 格式：[次数1,次数2...]
ETH_PREFIX_REPEAT_COUNT = [
    [8,9,10],   # 0:1位
    [5,6,7,8],        # 1:2位
    [4,5,8,9,10],           # 2:3位（你要的：3位重复4/5/8/9/10次）
    [3,4,5,6,7,8],        # 3:4位
    [3,4,5,6,7,8],        # 4:5位
    [2,3,4,5,6,7,8],        # 5:6位
    [2,3,4,5,6,7,8],        # 6:7位
    [2,3,4,5,6,7,8],                    # 7:8位（你要的：只重复2次）
    [2,3,4,5,6],                # 8:9位
    [2,3],                  # 9:10位
]

# -------------------------- 后缀重复（地址最后部分） --------------------------
# 例子：0x*****67896789 = 后缀4位重复2次
ETH_SUFFIX_REPEAT_ENABLE = True  # 后缀重复总开关

# 后缀：1~10位 单元是否开启
ETH_SUFFIX_LEN_ENABLE = [
    False,   # 0:1位
    True,   # 1:2位（你要的：开启）
    True,   # 2:3位
    True,   # 3:4位
    True,   # 4:5位
    True,   # 5:6位
    True,   # 6:7位
    True,   # 7:8位
    True,   # 8:9位
    True,   # 9:10位
]

# 后缀：每种长度允许的重复次数
ETH_SUFFIX_REPEAT_COUNT = [
    [8,9,10],   # 0:1位
    [5,6,7,8,9,10],         # 1:2位（你要的：2位重复5~10次）
    [4,5,6,7,8],        # 2:3位
    [3,4,5,6,7,8],        # 3:4位
    [3,4,5,6,7,8],        # 4:5位
    [2,3,4,5,6,7,8],        # 5:6位
    [2,3,4,5,6,7,8],        # 6:7位
    [2],                    # 7:8位（你要的：8位重复2次）
    [2,3,4],                # 8:9位
    [2,3],                  # 9:10位
]

# 大小写区分
ETH_PREFIX_SUFFIX_CASE_SENSITIVE = True

# ------------------------------ 【运行参数】 ------------------------------
PROCESS_NUM = 8
PROGRESS_REFRESH = 1
BATCH_UPDATE_THRESHOLD = 1000
SAVE_FILE_PATH = "save_address_eth.txt"
MNEMONIC_LANG = "english"

# ==============================================================================
# ============================ 依赖导入 ============================
# ==============================================================================
import time
import os
import signal
import threading
import sys
import traceback
import re
from multiprocessing import Pool, Lock, Value, set_start_method
import hashlib
import hmac
import binascii

try:
    set_start_method('fork')
except RuntimeError:
    pass

import mnemonic
from bip_utils import Bip39SeedGenerator, Bip44, Bip44Coins
from ecdsa import SigningKey, SECP256k1
from Crypto.Hash import keccak

# ==============================================================================
# ============================ 全局统计 ============================
# ==============================================================================
TOTAL_GENERATED = Value('i', 0)
TOTAL_FOUND = Value('i', 0)
START_TIME = time.time()
GLOBAL_LOCK = Lock()
IS_RUNNING = True
# ==============================================================================
# ============================ 工具函数 ============================
# ==============================================================================
def parse_number_sequence(s):
    nums, str_nums = [], []
    i, n = 0, len(s)
    while i < n:
        if i + 1 < n and s[i] == '1' and s[i+1].isdigit():
            num_str = s[i:i+2]
            nums.append(int(num_str))
            str_nums.append(num_str)
            i += 2
        elif s[i].isdigit():
            num_str = s[i]
            nums.append(int(num_str))
            str_nums.append(num_str)
            i += 1
        else:
            return None, None
    return nums, str_nums

def get_seq_position(addr_body, seq_str):
    if addr_body.startswith(seq_str):
        return "开头"
    elif addr_body.endswith(seq_str):
        return "结尾"
    elif addr_body == seq_str:
        return "全局"
    else:
        return "中间"

def count_continuous_repeats(s, seg_length):
    if len(s) < seg_length * 2:
        return None, 0
    max_count, max_seg = 0, ""
    i = 0
    while i <= len(s) - seg_length:
        current_seg = s[i:i+seg_length]
        if not (current_seg.isdigit() or current_seg.isalpha()):
            i += 1
            continue
        count = 1
        next_i = i + seg_length
        while next_i <= len(s) - seg_length and s[next_i:next_i+seg_length] == current_seg:
            count += 1
            next_i += seg_length
        if count > max_count:
            max_count, max_seg = count, current_seg
        i = next_i if count > 1 else i + 1
    return max_seg, max_count

# ==============================================================================
# ====================== 【新增】前缀/后缀重复模式检测 ==========================
# ==============================================================================
def check_prefix_suffix_repeat(addr_body):
    if not ETH_PREFIX_SUFFIX_REPEAT_ENABLE:
        return False, ""

    body = addr_body
    reason = ""

    # -------------------------- 前缀检测 --------------------------
    if ETH_PREFIX_REPEAT_ENABLE:
        for length_idx in range(10):
            L = length_idx + 1
            if not ETH_PREFIX_LEN_ENABLE[length_idx]:
                continue
            allowed_counts = ETH_PREFIX_REPEAT_COUNT[length_idx]
            if len(body) < L * 2:
                continue

            unit = body[:L]
            full_repeat = unit
            count = 1
            while len(full_repeat) + L <= len(body):
                next_part = body[len(full_repeat) : len(full_repeat)+L]
                if not ETH_PREFIX_SUFFIX_CASE_SENSITIVE:
                    next_part = next_part.lower()
                    unit_check = unit.lower()
                else:
                    unit_check = unit
                if next_part == unit_check:
                    count += 1
                    full_repeat += next_part
                else:
                    break
            if count in allowed_counts:
                reason = f"前缀{L}位重复{count}次：{unit}"
                return True, reason

    # -------------------------- 后缀检测 --------------------------
    if ETH_SUFFIX_REPEAT_ENABLE:
        for length_idx in range(10):
            L = length_idx + 1
            if not ETH_SUFFIX_LEN_ENABLE[length_idx]:
                continue
            allowed_counts = ETH_SUFFIX_REPEAT_COUNT[length_idx]
            if len(body) < L * 2:
                continue

            unit = body[-L:]
            count = 1
            pos = len(body) - L
            while pos - L >= 0:
                next_part = body[pos-L : pos]
                if not ETH_PREFIX_SUFFIX_CASE_SENSITIVE:
                    next_part = next_part.lower()
                    unit_check = unit.lower()
                else:
                    unit_check = unit
                if next_part == unit_check:
                    count += 1
                    pos -= L
                else:
                    break
            if count in allowed_counts:
                reason = f"后缀{L}位重复{count}次：{unit}"
                return True, reason

    return False, reason

# ==============================================================================
# ============================ 信号处理 & 进度刷新 ============================
# ==============================================================================
def signal_handler(sig, frame):
    global IS_RUNNING
    IS_RUNNING = False
    time.sleep(0.5)
    elapsed = time.time() - START_TIME
    os.system('clear' if os.name == 'posix' else 'cls')
    print("="*80)
    print("程序终止 - ETH 靓号生成器")
    print(f"累计生成：{TOTAL_GENERATED.value:,}")
    print(f"累计找到：{TOTAL_FOUND.value}")
    print(f"速度：{int(TOTAL_GENERATED.value/elapsed) if elapsed>0 else 0} 个/秒")
    print("="*80)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def progress_refresher():
    last_gen = 0
    while IS_RUNNING:
        time.sleep(PROGRESS_REFRESH)
        elapsed = time.time() - START_TIME
        with TOTAL_GENERATED.get_lock():
            current_gen = TOTAL_GENERATED.value
        with TOTAL_FOUND.get_lock():
            current_found = TOTAL_FOUND.value
        speed = int((current_gen - last_gen) / PROGRESS_REFRESH) if elapsed > 0 else 0
        last_gen = current_gen
        os.system('clear' if os.name == 'posix' else 'cls')
        print("="*80)
        print("🔥 ETH 靓号扫描器（支持前缀/后缀重复模式）")
        print(f"进程：{PROCESS_NUM} | 结果文件：{SAVE_FILE_PATH}")
        print(f"已生成：{current_gen:,} | 速度：{speed}/s | 命中：{current_found}")
        print("="*80)
        sys.stdout.flush()

# ==============================================================================
# ============================ 原有规则函数 ============================
# ==============================================================================
def check_seq_0_9(s, is_reverse=False):
    min_len = ETH_SEQ_0_9_MIN_LEN if not is_reverse else ETH_REV_SEQ_0_9_MIN_LEN
    if len(s) < min_len:
        return False, "", ""
    for i in range(len(s) - min_len + 1):
        sub_str = s[i:i+min_len]
        if not sub_str.isdigit():
            continue
        nums = [int(c) for c in sub_str]
        is_seq = True
        if not is_reverse:
            for j in range(1, len(nums)):
                if (nums[j] - nums[j-1]) % 10 != 1:
                    is_seq = False
                    break
        else:
            for j in range(1, len(nums)):
                if (nums[j-1] - nums[j]) % 10 != 1:
                    is_seq = False
                    break
        if is_seq:
            max_seq_str = sub_str
            k = i + min_len
            while k < len(s):
                next_char = s[k]
                if not next_char.isdigit():
                    break
                next_num = int(next_char)
                if not is_reverse:
                    if (next_num - int(max_seq_str[-1])) % 10 == 1:
                        max_seq_str += next_char
                        k += 1
                    else:
                        break
                else:
                    if (int(max_seq_str[-1]) - next_num) % 10 == 1:
                        max_seq_str += next_char
                        k += 1
                    else:
                        break
            return True, max_seq_str, get_seq_position(s, max_seq_str)
    return False, "", ""

def check_seq_0_10(s, is_reverse=False):
    min_len = ETH_SEQ_0_10_MIN_LEN if not is_reverse else ETH_REV_SEQ_0_10_MIN_LEN
    if len(s) < min_len:
        return False, "", ""
    nums, str_nums = parse_number_sequence(s)
    if not nums or len(nums) < min_len:
        return False, "", ""
    if not is_reverse:
        for i in range(len(nums) - min_len + 1):
            sub_nums = nums[i:i+min_len]
            if all(sub_nums[j] - sub_nums[j-1] == 1 for j in range(1, len(sub_nums))):
                seq_str = ''.join(str_nums[i:i+min_len])
                max_seq_idx = i + min_len
                while max_seq_idx < len(nums) and nums[max_seq_idx] - nums[max_seq_idx-1] == 1:
                    seq_str += str_nums[max_seq_idx]
                    max_seq_idx += 1
                return True, seq_str, get_seq_position(s, seq_str)
    else:
        for i in range(len(nums) - min_len + 1):
            sub_nums = nums[i:i+min_len]
            if all(sub_nums[j-1] - sub_nums[j] == 1 for j in range(1, len(sub_nums))):
                seq_str = ''.join(str_nums[i:i+min_len])
                max_seq_idx = i + min_len
                while max_seq_idx < len(nums) and nums[max_seq_idx-1] - nums[max_seq_idx] == 1:
                    seq_str += str_nums[max_seq_idx]
                    max_seq_idx += 1
                return True, seq_str, get_seq_position(s, seq_str)
    return False, "", ""

def check_first10_rules(addr_body):
    if not ETH_FIRST10_ENABLE or len(addr_body) < 10:
        return False, ""
    first2 = addr_body[:2]
    check_first2 = first2 if ETH_FIRST2_CASE_SENSITIVE else first2.lower()
    target_first2 = [s if ETH_FIRST2_CASE_SENSITIVE else s.lower() for s in ETH_FIRST2_POOL]
    if check_first2 not in target_first2:
        return False, ""
    first3_10 = addr_body[2:10]
    match_reason = ""
    if ETH_FIRST3_10_BOMB_ENABLE:
        check_bomb = first3_10 if ETH_FIRST3_10_BOMB_CASE_SENSITIVE else first3_10.lower()
        target_bomb = [s if ETH_FIRST3_10_BOMB_CASE_SENSITIVE else s.lower() for s in ETH_FIRST3_10_BOMB_POOL]
        if check_bomb in target_bomb:
            match_reason = f"前10位-双炸弹：{first3_10}"
    if not match_reason and ETH_FIRST3_10_SEQ_ENABLE:
        check_seq = first3_10 if ETH_FIRST3_10_SEQ_CASE_SENSITIVE else first3_10.lower()
        target_seq = [s if ETH_FIRST3_10_SEQ_CASE_SENSITIVE else s.lower() for s in ETH_FIRST3_10_SEQ_POOL]
        if check_seq in target_seq:
            match_reason = f"前10位-顺子：{first3_10}"
    if not match_reason and ETH_FIRST3_10_DOUBLE_CHAR_ENABLE:
        check_double = first3_10 if ETH_FIRST3_10_DOUBLE_CHAR_CASE_SENSITIVE else first3_10.lower()
        target_double = [s if ETH_FIRST3_10_DOUBLE_CHAR_CASE_SENSITIVE else s.lower() for s in ETH_FIRST3_10_DOUBLE_CHAR_POOL]
        if check_double in target_double:
            match_reason = f"前10位-双字符：{first3_10}"
    if not match_reason and ETH_FIRST3_10_PALINDROME_ENABLE:
        check_pali = first3_10 if ETH_FIRST3_10_PALINDROME_CASE_SENSITIVE else first3_10.lower()
        target_pali = [s if ETH_FIRST3_10_PALINDROME_CASE_SENSITIVE else s.lower() for s in ETH_FIRST3_10_PALINDROME_POOL]
        if check_pali in target_pali:
            match_reason = f"前10位-回文：{first3_10}"
    return bool(match_reason), f"前10位规则匹配（前2位：{first2}，{match_reason}）" if match_reason else ""

def check_last10_rules(addr_body):
    if not ETH_LAST10_ENABLE or len(addr_body) < 10:
        return False, ""
    last2 = addr_body[-2:]
    check_last2 = last2 if ETH_LAST2_CASE_SENSITIVE else last2.lower()
    target_last2 = [s if ETH_LAST2_CASE_SENSITIVE else s.lower() for s in ETH_LAST2_POOL]
    if check_last2 not in target_last2:
        return False, ""
    last3_10 = addr_body[-10:-2] if len(addr_body) >= 10 else ""
    if len(last3_10) != 8:
        return False, ""
    match_reason = ""
    if ETH_LAST3_10_BOMB_ENABLE:
        check_bomb = last3_10 if ETH_LAST3_10_BOMB_CASE_SENSITIVE else last3_10.lower()
        target_bomb = [s if ETH_LAST3_10_BOMB_CASE_SENSITIVE else s.lower() for s in ETH_LAST3_10_BOMB_POOL]
        if check_bomb in target_bomb:
            match_reason = f"末尾10位-双炸弹：{last3_10}"
    if not match_reason and ETH_LAST3_10_SEQ_ENABLE:
        check_seq = last3_10 if ETH_LAST3_10_SEQ_CASE_SENSITIVE else last3_10.lower()
        target_seq = [s if ETH_LAST3_10_SEQ_CASE_SENSITIVE else s.lower() for s in ETH_LAST3_10_SEQ_POOL]
        if check_seq in target_seq:
            match_reason = f"末尾10位-顺子：{last3_10}"
    if not match_reason and ETH_LAST3_10_DOUBLE_CHAR_ENABLE:
        check_double = last3_10 if ETH_LAST3_10_DOUBLE_CHAR_CASE_SENSITIVE else last3_10.lower()
        target_double = [s if ETH_LAST3_10_DOUBLE_CHAR_CASE_SENSITIVE else s.lower() for s in ETH_LAST3_10_DOUBLE_CHAR_POOL]
        if check_double in target_double:
            match_reason = f"末尾10位-双字符：{last3_10}"
    if not match_reason and ETH_LAST3_10_PALINDROME_ENABLE:
        check_pali = last3_10 if ETH_LAST3_10_PALINDROME_CASE_SENSITIVE else last3_10.lower()
        target_pali = [s if ETH_LAST3_10_PALINDROME_CASE_SENSITIVE else s.lower() for s in ETH_LAST3_10_PALINDROME_POOL]
        if check_pali in target_pali:
            match_reason = f"末尾10位-回文：{last3_10}"
    return bool(match_reason), f"末尾10位规则匹配（最后2位：{last2}，{match_reason}）" if match_reason else ""

def check_40char_rules(addr_body):
    if not ETH_40CHAR_RULE_ENABLE or len(addr_body) != 40:
        return False, ""
    match_details = []
    for (start, end, char_pool, case_sensitive, special_rule) in ETH_40CHAR_SEGMENTS:
        if start < 1 or end > 40 or start > end:
            continue
        seg_chars = addr_body[start-1:end]
        if special_rule == "EVEN=8":
            for pos in range(start, end+1):
                char_idx = pos - 1
                if pos % 2 == 0:
                    if addr_body[char_idx] != "8":
                        return False, ""
                    match_details.append(f"第{pos}位(偶数位)=8")
        elif special_rule and "ODD=" in special_rule:
            odd_chars = special_rule.split("=")[1]
            for pos in range(start, end+1):
                char_idx = pos - 1
                if pos % 2 == 1:
                    char = addr_body[char_idx]
                    check_char = char if case_sensitive else char.lower()
                    check_pool = odd_chars if case_sensitive else odd_chars.lower()
                    if check_char not in check_pool:
                        return False, ""
                    match_details.append(f"第{pos}位(奇数位)={char}(属于{odd_chars})")
        if char_pool:
            for pos_in_seg, char in enumerate(seg_chars):
                global_pos = start + pos_in_seg
                check_char = char if case_sensitive else char.lower()
                check_pool = char_pool if case_sensitive else char_pool.lower()
                if check_char not in check_pool:
                    return False, ""
                match_details.append(f"第{global_pos}位={char}(属于{char_pool})")
    if match_details:
        reason = f"40位精细化规则匹配：{'; '.join(match_details[:5])}..."
        return True, reason
    return False, ""

def format_vanity_type(reason, addr_body_output):
    if "前缀" in reason or "后缀" in reason:
        return f"ETH+{reason}"
    if "40位精细化规则匹配" in reason:
        return "ETH+40位精细化字符规则+" + reason.split("：")[1][:50] + "..."
    if "1位数字" in reason and "重复" in reason:
        seg = reason.split("1位数字")[1].split("重复")[0]
        times = reason.split("重复")[1].split("次")[0]
        repeat_type = "连续重复" if ETH_1CHAR_REPEAT_MUST_CONTINUOUS else "非连续重复"
        return f"ETH+全局+{repeat_type}+1位数字{seg}×{times}"
    return f"ETH+{reason}"

# ==============================================================================
# ============================ 核心检测 ============================
# ==============================================================================
def check_vanity_patterns(addr):
    addr_body = addr[2:]
    reason = ""
    original_rule_matched = False

    # 【新功能：前缀/后缀重复（最高优先级）】
    if not original_rule_matched:
        ps_match, ps_reason = check_prefix_suffix_repeat(addr_body)
        if ps_match:
            original_rule_matched = True
            reason = ps_reason

    # 以下原有逻辑完全不变
    if not original_rule_matched and len(addr_body) == 40:
        char40_matched, char40_reason = check_40char_rules(addr_body)
        if char40_matched:
            original_rule_matched = True
            reason = char40_reason

    if not original_rule_matched:
        first10_matched, first10_reason = check_first10_rules(addr_body)
        if first10_matched:
            original_rule_matched = True
            reason = first10_reason

    if not original_rule_matched:
        last10_matched, last10_reason = check_last10_rules(addr_body)
        if last10_matched:
            original_rule_matched = True
            reason = last10_reason

    if not original_rule_matched:
        if ETH_CHECK_FULL_NUM and addr_body.isdigit():
            reason = "纯数字地址"
            original_rule_matched = True
        elif ETH_CHECK_FULL_ALPHA and addr_body.isalpha():
            reason = "纯字母地址"
            original_rule_matched = True

    if not original_rule_matched:
        exclude_ok = True
        if ETH_EXCLUDE_CHARS_ENABLE:
            if any(c in addr_body for c in ETH_EXCLUDE_CHARS):
                exclude_ok = False
        only_allow_ok = not ETH_ONLY_ALLOW_CHARS_ENABLE
        if ETH_ONLY_ALLOW_CHARS_ENABLE:
            for allowed in ETH_ONLY_ALLOW_CHARS_LIST:
                if all(c in allowed for c in addr_body):
                    only_allow_ok = True
                    break
        if exclude_ok and only_allow_ok:
            if ETH_EXCLUDE_CHARS_ENABLE or ETH_ONLY_ALLOW_CHARS_ENABLE:
                reason = ""
                if ETH_EXCLUDE_CHARS_ENABLE:
                    reason += f"不包含指定字符：{ETH_EXCLUDE_CHARS} "
                if ETH_ONLY_ALLOW_CHARS_ENABLE:
                    reason += f"仅包含指定字符组合：{','.join(ETH_ONLY_ALLOW_CHARS_LIST)}"
                original_rule_matched = True

    if not original_rule_matched:
        if ETH_1DIGIT_REPEAT_CHECK:
            target_digits = [str(d) for d in range(10)]
            for d in target_digits:
                cnt = addr_body.count(d)
                if cnt >= ETH_1DIGIT_REPEAT_MIN:
                    if ETH_1CHAR_REPEAT_MUST_CONTINUOUS:
                        if d*ETH_1DIGIT_REPEAT_MIN in addr_body:
                            reason = f"1位数字{d}重复{cnt}次"
                            original_rule_matched = True
                            break
                    else:
                        reason = f"1位数字{d}重复{cnt}次"
                        original_rule_matched = True
                        break
        if not original_rule_matched and ETH_1ALPHA_REPEAT_CHECK:
            target_alphas = [chr(ord('a')+i) for i in range(26)] + [chr(ord('A')+i) for i in range(26)]
            for a in target_alphas:
                check_a = a if ETH_ALPHA_CASE_SENSITIVE else a.lower()
                check_body = addr_body if ETH_ALPHA_CASE_SENSITIVE else addr_body.lower()
                cnt = check_body.count(check_a)
                if cnt >= ETH_1ALPHA_REPEAT_MIN:
                    if ETH_1CHAR_REPEAT_MUST_CONTINUOUS:
                        if check_a*ETH_1ALPHA_REPEAT_MIN in check_body:
                            reason = f"1位字母{a}重复{cnt}次"
                            original_rule_matched = True
                            break
                    else:
                        reason = f"1位字母{a}重复{cnt}次"
                        original_rule_matched = True
                        break

    if not original_rule_matched:
        def check_long_run(s, is_digit):
            max_len = 0
            max_char = ''
            current = s[0]
            current_len = 1
            for c in s[1:]:
                if c == current:
                    current_len += 1
                else:
                    if current_len > max_len:
                        max_len = current_len
                        max_char = current
                    current = c
                    current_len = 1
            if current_len > max_len:
                max_len = current_len
                max_char = current
            return max_char, max_len

        start_char = addr_body[0]
        start_cnt = 1
        for c in addr_body[1:]:
            if c == start_char:
                start_cnt += 1
            else:
                break
        if start_char.isdigit() and start_cnt >= ETH_START_DIGIT_SAME:
            reason = f"开头{start_cnt}位相同数字：{start_char}"
            original_rule_matched = True
        elif start_char.isalpha() and start_cnt >= ETH_START_ALPHA_SAME:
            reason = f"开头{start_cnt}位相同字母：{start_char}"
            original_rule_matched = True

        if not original_rule_matched:
            end_char = addr_body[-1]
            end_cnt = 1
            for c in reversed(addr_body[:-1]):
                if c == end_char:
                    end_cnt += 1
                else:
                    break
            if end_char.isdigit() and end_cnt >= ETH_END_DIGIT_SAME:
                reason = f"结尾{end_cnt}位相同数字：{end_char}"
                original_rule_matched = True
            elif end_char.isalpha() and end_cnt >= ETH_END_ALPHA_SAME:
                reason = f"结尾{end_cnt}位相同字母：{end_char}"
                original_rule_matched = True

        if not original_rule_matched:
            mid_char, mid_len = check_long_run(addr_body, is_digit=True)
            if mid_len >= ETH_MID_DIGIT_SAME:
                reason = f"中间{mid_len}位相同数字：{mid_char}"
                original_rule_matched = True
            else:
                mid_char, mid_len = check_long_run(addr_body, is_digit=False)
                if mid_len >= ETH_MID_ALPHA_SAME:
                    reason = f"中间{mid_len}位相同字母：{mid_char}"
                    original_rule_matched = True

    if not original_rule_matched:
        for length in range(2, 11):
            if original_rule_matched:
                break
            check_digit = globals().get(f"ETH_{length}DIGIT_REPEAT_CHECK", False)
            min_digit = globals().get(f"ETH_{length}DIGIT_REPEAT_MIN", 2)
            if check_digit:
                seg, count = count_continuous_repeats(addr_body, length)
                if count >= min_digit:
                    reason = f"{length}位数字{seg}重复{count}次"
                    original_rule_matched = True
                    break
            check_alpha = globals().get(f"ETH_{length}ALPHA_REPEAT_CHECK", False)
            min_alpha = globals().get(f"ETH_{length}ALPHA_REPEAT_MIN", 2)
            if check_alpha and not original_rule_matched:
                seg, count = count_continuous_repeats(addr_body, length)
                if count >= min_alpha:
                    reason = f"{length}位字母{seg}重复{count}次"
                    original_rule_matched = True
                    break

    if not original_rule_matched:
        if ETH_SEQ_0_9_ENABLE:
            ok, seq, pos = check_seq_0_9(addr_body, is_reverse=False)
            if ok:
                reason = f"0~9正顺（{pos}，{len(seq)}位：{seq}）"
                original_rule_matched = True
        if not original_rule_matched and ETH_REV_SEQ_0_9_ENABLE:
            ok, seq, pos = check_seq_0_9(addr_body, is_reverse=True)
            if ok:
                reason = f"0~9倒顺（{pos}，{len(seq)}位：{seq}）"
                original_rule_matched = True
        if not original_rule_matched and ETH_SEQ_0_10_ENABLE:
            ok, seq, pos = check_seq_0_10(addr_body, is_reverse=False)
            if ok:
                reason = f"0~10正顺（{pos}，{len(seq)}位：{seq}）"
                original_rule_matched = True
        if not original_rule_matched and ETH_REV_SEQ_0_10_ENABLE:
            ok, seq, pos = check_seq_0_10(addr_body, is_reverse=True)
            if ok:
                reason = f"0~10倒顺（{pos}，{len(seq)}位：{seq}）"
                original_rule_matched = True

    if not original_rule_matched and ETH_CUSTOM_STR_ENABLE:
        custom_list = ETH_CUSTOM_STR.strip("{}").split(";")
        for s in custom_list:
            if not s:
                continue
            check_addr = addr_body if ETH_CUSTOM_STR_CASE_SENSITIVE else addr_body.lower()
            check_s = s if ETH_CUSTOM_STR_CASE_SENSITIVE else s.lower()
            found = False
            pos = ""
            if ETH_CUSTOM_STR_START_ENABLE and check_addr.startswith(check_s):
                found = True
                pos = "开头"
            elif ETH_CUSTOM_STR_END_ENABLE and check_addr.endswith(check_s):
                found = True
                pos = "结尾"
            elif ETH_CUSTOM_STR_ANY_ENABLE and check_s in check_addr:
                found = True
                pos = "任意位置"
            if found:
                reason = f"包含自定义字符串：{s}（{pos}）"
                original_rule_matched = True
                break

    if not original_rule_matched:
        return False, "", ""

    if ETH_ADDR_OUTPUT_CASE == "upper":
        addr_body_output = addr_body.upper()
    elif ETH_ADDR_OUTPUT_CASE == "lower":
        addr_body_output = addr_body.lower()
    else:
        addr_body_output = addr_body
    addr_output = "0x" + addr_body_output

    vanity_type = format_vanity_type(reason, addr_body_output)
    return True, addr_output, vanity_type

# ==============================================================================
# ============================ 地址生成 & 工作进程 ============================
# ==============================================================================
def generate_eth_address():
    try:
        mnemo = mnemonic.Mnemonic(MNEMONIC_LANG)
        words = mnemo.generate(strength=256)
        seed = Bip39SeedGenerator(words).Generate()
        eth_ctx = Bip44.FromSeed(seed, Bip44Coins.ETHEREUM).DeriveDefaultPath()
        eth_addr = eth_ctx.PublicKey().ToAddress()
        return eth_addr, words
    except:
        time.sleep(0.001)
        return generate_eth_address()

def worker(_):
    batch = []
    cnt = 0
    while IS_RUNNING:
        try:
            eth_addr, eth_words = generate_eth_address()
            is_vanity_eth, eth_addr_output, vanity_type_eth = check_vanity_patterns(eth_addr)
            with TOTAL_GENERATED.get_lock():
                TOTAL_GENERATED.value += 1
            cnt += 1

            now = time.strftime("%Y-%m-%d %H:%M:%S")
            lines = []
            if is_vanity_eth:
                lines.append(f"\n=== ETH靓号发现 | 生成时间：{now} ===")
                lines.append(f"靓号类型：{vanity_type_eth}")
                lines.append(f"ETH地址：{eth_addr_output}")
                lines.append(f"24词助记词：{eth_words}")
                lines.append("-" * 70)

            if lines:
                batch.append("\n".join(lines))
                with TOTAL_FOUND.get_lock():
                    TOTAL_FOUND.value += 1

            if cnt >= BATCH_UPDATE_THRESHOLD or len(batch) >= 10:
                if batch:
                    with GLOBAL_LOCK:
                        with open(SAVE_FILE_PATH, "a", encoding="utf-8") as f:
                            f.write("\n".join(batch) + "\n")
                    batch = []
                cnt = 0
        except Exception as e:
            time.sleep(0.1)
            continue

# ==============================================================================
# ============================ 主程序入口 ============================
# ==============================================================================
if __name__ == "__main__":
    if not os.path.exists(SAVE_FILE_PATH):
        with open(SAVE_FILE_PATH, "w", encoding="utf-8") as f:
            f.write("="*80 + "\n")
            f.write("ETH靓号地址（24词助记词｜前缀/后缀重复模式｜完整版）\n")
            f.write(f"文件创建时间：{time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("规则包含：前缀重复 | 后缀重复 | 顺子 | 重复字符 | 自定义字符串 | 40位精细化规则\n")
            f.write("⚠️  助记词是资产唯一凭证，请离线保管，切勿泄露！\n")
            f.write("="*80 + "\n\n")

    threading.Thread(target=progress_refresher, daemon=True).start()
    time.sleep(0.5)

    try:
        with Pool(processes=PROCESS_NUM) as pool:
            pool.map(worker, range(PROCESS_NUM))
    except KeyboardInterrupt:
        signal_handler(signal.SIGINT, None)
    except Exception as e:
        print(f"主程序异常：{str(e)}")
        IS_RUNNING = False
        sys.exit(1)