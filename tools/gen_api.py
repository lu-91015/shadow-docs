#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成 shadow 0.5 API 文档：
  - 内置函数（编译器原语，白名单见 src/type_checker/type_checker.shadow
    tc_builtin_ret_type，签名经 rt/*.c 运行时与源码用法核实）
  - 标准库（src/std 各包，直接抽取 pub kimo 真实签名）

产出到 shadow-docs/docs/api/：
  index.md                  库参考总览
  builtins/<name>.md        每个内置函数单独一页（入参 / 出参 / 示例）
  std/<pkg>.md              每个标准库包一页（列出全部 pub 函数）
"""
import os
import re
import sys

# ---- 路径（与 shadow-0.5 仓库对齐）---------------------------------------
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs", "api")
# shadow-0.5 仓库根（std 源码在此）
SHADOW05 = r"C:/Users/cxyu/AppData/Roaming/TRAE SOLO CN/ModularData/ai-agent/work-mode-projects/6a5353846df2d3b188c57699/shadow/shadow-0.5"
STD_DIR = os.path.join(SHADOW05, "std")

# ---- 内置函数表（已核实）--------------------------------------------------
# params: [(name, type, desc), ...]；ret: (type, desc)
BUILTINS = [
    # 输出
    dict(name="println", cat="输出", params=[("args", "...", "任意类型，多个以空格分隔，末尾换行")],
         ret=("()", "无返回值（unit）"),
         desc="向标准输出打印参数，自动按类型格式化并在末尾追加换行。",
         example='println("hello", 42, true);'),
    dict(name="print", cat="输出", params=[("args", "...", "任意类型，多个以空格分隔，不换行")],
         ret=("()", "无返回值（unit）"),
         desc="向标准输出打印参数，自动按类型格式化，不追加换行。",
         example='print("loading");'),
    dict(name="len", cat="输出", params=[("x", "any", "数组 / 字符串 / 集合 / 字典等可度量长度的值")],
         ret=("int", "元素个数"),
         desc="返回容器或字符串的长度（字符数 / 元素数）。",
         example='let n = len("abc");  // 3'),

    # 类型转换
    dict(name="to_string", cat="类型转换", params=[("x", "any", "任意可格式化的值")],
         ret=("string", "字符串形式"),
         desc="将任意值转换为字符串（等价于 str）。",
         example='let s = to_string(42);'),
    dict(name="str", cat="类型转换", params=[("x", "any", "任意可格式化的值")],
         ret=("string", "字符串形式"),
         desc="将任意值转换为字符串（to_string 的别名）。",
         example='let s = str(3.14);'),
    dict(name="int_to_str", cat="类型转换", params=[("i", "int", "整数")],
         ret=("string", "十进制字符串"),
         desc="将 int 转换为十进制字符串。",
         example='let s = int_to_str(42);  // "42"'),
    dict(name="long_to_str", cat="类型转换", params=[("i", "long", "长整数")],
         ret=("string", "十进制字符串"),
         desc="将 long 转换为十进制字符串。",
         example='let s = long_to_str(9000000000L);'),
    dict(name="float_to_str", cat="类型转换", params=[("f", "float", "单精度浮点")],
         ret=("string", "字符串形式"),
         desc="将 float 转换为字符串。",
         example='let s = float_to_str(1.5f);'),
    dict(name="double_to_str", cat="类型转换", params=[("d", "double", "双精度浮点")],
         ret=("string", "字符串形式"),
         desc="将 double 转换为字符串。",
         example='let s = double_to_str(3.14159);'),
    dict(name="bool_to_str", cat="类型转换", params=[("b", "bool", "布尔值")],
         ret=("string", '"true" 或 "false"'),
         desc="将 bool 转换为 \"true\"/\"false\"。",
         example='let s = bool_to_str(true);'),
    dict(name="char_to_str", cat="类型转换", params=[("c", "char", "字符")],
         ret=("string", "单字符字符串"),
         desc="将 char 转换为单字符字符串。",
         example='let s = char_to_str(\'A\');'),

    # 数组
    dict(name="array_push", cat="数组", params=[("arr", "array<T>", "目标数组"), ("elems", "...", "一个或多个待追加元素（类型须与数组元素一致）")],
         ret=("array<T>", "追加后的数组"),
         desc="将元素追加到数组末尾，返回新数组（可变长）。",
         example='parts = array_push(parts, "x");'),

    # 字符串处理
    dict(name="substr2", cat="字符串处理", params=[("s", "string", "源字符串"), ("start", "int", "起始下标（0 基）"), ("n", "int", "长度")],
         ret=("string", "子串"),
         desc="取从 start 开始、长度为 n 的子串。",
         example='let sub = substr2("hello", 1, 3);  // "ell"'),
    dict(name="str_replace", cat="字符串处理", params=[("s", "string", "源字符串"), ("from", "string", "被替换子串"), ("to", "string", "替换后的子串")],
         ret=("string", "替换后的字符串"),
         desc="将 s 中所有 from 替换为 to。",
         example='let r = str_replace("a-b-c", "-", ".");  // "a.b.c"'),
    dict(name="str_trim", cat="字符串处理", params=[("s", "string", "源字符串")],
         ret=("string", "去空白后的字符串"),
         desc="去除首尾空白字符。",
         example='let r = str_trim("  hi  ");  // "hi"'),
    dict(name="str_to_upper", cat="字符串处理", params=[("s", "string", "源字符串")],
         ret=("string", "全大写"),
         desc="将字符串转为大写。",
         example='let r = str_to_upper("abc");  // "ABC"'),
    dict(name="str_to_lower", cat="字符串处理", params=[("s", "string", "源字符串")],
         ret=("string", "全小写"),
         desc="将字符串转为小写。",
         example='let r = str_to_lower("ABC");  // "abc"'),
    dict(name="str_char_at", cat="字符串处理", params=[("s", "string", "源字符串"), ("idx", "int", "下标（负索引回绕，越界返回空串）")],
         ret=("string", "单字符子串"),
         desc="取第 idx 个字符（返回单字符字符串）。",
         example='let c = str_char_at("abc", 1);  // "b"'),
    dict(name="str_join", cat="字符串处理", params=[("parts", "array<string>", "片段列表"), ("sep", "string", "连接符")],
         ret=("string", "拼接结果"),
         desc="用 sep 将字符串数组连接成一个字符串。",
         example='let s = str_join(parts, ",");'),
    dict(name="str_format", cat="字符串处理", params=[("fmt", "string", "含 {0}{1}… 占位符的模板"), ("args", "array<string>", "占位符对应的实参")],
         ret=("string", "格式化结果"),
         desc="按 {N} 占位符格式化；{{/}} 转义字面花括号；非法索引保留原样。",
         example='let s = str_format("{0}+{1}", ["a", "b"]);  // "a+b"'),
    dict(name="str_contains", cat="字符串处理", params=[("s", "string", "源字符串"), ("sub", "string", "子串")],
         ret=("int", "包含为 1，否则 0"),
         desc="判断 s 是否包含子串 sub。",
         example='if (str_contains("abc", "b") == 1) { }'),
    dict(name="str_index_of", cat="字符串处理", params=[("s", "string", "源字符串"), ("sub", "string", "子串")],
         ret=("int", "首次出现下标，未找到返回 -1"),
         desc="返回 sub 在 s 中首次出现的下标。",
         example='let i = str_index_of("abc", "b");  // 1'),
    dict(name="str_starts_with", cat="字符串处理", params=[("s", "string", "源字符串"), ("prefix", "string", "前缀")],
         ret=("int", "是则 1，否则 0"),
         desc="判断 s 是否以 prefix 开头。",
         example='if (str_starts_with("file.txt", "file") == 1) { }'),
    dict(name="str_ends_with", cat="字符串处理", params=[("s", "string", "源字符串"), ("suffix", "string", "后缀")],
         ret=("int", "是则 1，否则 0"),
         desc="判断 s 是否以 suffix 结尾。",
         example='if (str_ends_with("file.txt", ".txt") == 1) { }'),
    dict(name="str_split", cat="字符串处理", params=[("s", "string", "源字符串"), ("sep", "string", "分隔符")],
         ret=("array<string>", "分割后的片段列表"),
         desc="按 sep 分割字符串为字符串数组。",
         example='let parts = str_split("a,b,c", ",");'),
    dict(name="str_eq", cat="字符串处理", params=[("a", "string", "左操作数"), ("b", "string", "右操作数")],
         ret=("int", "相等为 1，否则 0"),
         desc="比较两个字符串是否相等（等价于 ==）。",
         example='if (str_eq(a, b) == 1) { }'),

    # 文件
    dict(name="file_read", cat="文件", params=[("path", "string", "文件路径")],
         ret=("string", "文件全部内容（读取失败返回空串）"),
         desc="读取文本文件的全部内容。",
         example='let src = file_read("main.shadow");'),
    dict(name="file_write", cat="文件", params=[("path", "string", "文件路径"), ("content", "string", "写入内容")],
         ret=("int", "成功为 0，失败为 -1"),
         desc="将内容写入文件（覆盖）。",
         example='file_write("out.txt", "hi");'),
    dict(name="file_exists", cat="文件", params=[("path", "string", "文件路径")],
         ret=("int", "存在为 1，否则 0"),
         desc="判断文件是否存在。",
         example='if (file_exists("a.txt") == 1) { }'),
    dict(name="file_delete", cat="文件", params=[("path", "string", "文件路径")],
         ret=("int", "成功为 0，失败为 -1"),
         desc="删除文件。",
         example='file_delete("a.txt");'),
    dict(name="file_list_dir", cat="文件", params=[("path", "string", "目录路径")],
         ret=("string", "分号分隔的目录条目列表"),
         desc="列出目录条目，以分号分隔（可用 str_split 拆开）。",
         example='let items = str_split(file_list_dir("."), ";");'),

    # 目录 / 路径
    dict(name="dir_create", cat="目录 / 路径", params=[("path", "string", "目录路径")],
         ret=("int", "成功为 0，失败为 -1"),
         desc="创建目录。",
         example='dir_create("build");'),
    dict(name="dir_delete", cat="目录 / 路径", params=[("path", "string", "目录路径")],
         ret=("int", "成功为 0，失败为 -1"),
         desc="删除目录。",
         example='dir_delete("build");'),
    dict(name="dir_exists", cat="目录 / 路径", params=[("path", "string", "目录路径")],
         ret=("int", "存在为 1，否则 0"),
         desc="判断目录是否存在。",
         example='if (dir_exists("src") == 1) { }'),
    dict(name="path_exists", cat="目录 / 路径", params=[("path", "string", "路径")],
         ret=("int", "存在为 1，否则 0"),
         desc="判断任意路径（文件或目录）是否存在。",
         example='if (path_exists("a.txt") == 1) { }'),
    dict(name="path_join", cat="目录 / 路径", params=[("base", "string", "基础路径"), ("child", "string", "子路径")],
         ret=("string", "拼接后的路径"),
         desc="跨平台地拼接路径分量。",
         example='let p = path_join("a", "b.txt");  // "a/b.txt"'),
    dict(name="path_dirname", cat="目录 / 路径", params=[("path", "string", "路径")],
         ret=("string", "父目录"),
         desc="返回路径的目录部分。",
         example='let d = path_dirname("a/b.txt");  // "a"'),
    dict(name="path_basename", cat="目录 / 路径", params=[("path", "string", "路径")],
         ret=("string", "文件名"),
         desc="返回路径的文件名部分。",
         example='let f = path_basename("a/b.txt");  // "b.txt"'),
    dict(name="path_normalize", cat="目录 / 路径", params=[("path", "string", "路径")],
         ret=("string", "规范化后的路径"),
         desc="规范化路径（解析 . / .. 与冗余分隔符）。",
         example='let p = path_normalize("a/./b/../c");  // "a/c"'),

    # 哈希表（dict）
    dict(name="hashmap_new", cat="哈希表", params=[],
         ret=("dict", "空字典（字符串键 → 字符串值）"),
         desc="创建一个空字典。",
         example='let m = hashmap_new();'),
    dict(name="hashmap_insert", cat="哈希表", params=[("map", "dict", "字典"), ("key", "string", "键"), ("value", "string", "值")],
         ret=("int", "成功为 0"),
         desc="向字典插入键值对（覆盖已有键）。",
         example='hashmap_insert(m, "k", "v");'),
    dict(name="hashmap_get", cat="哈希表", params=[("map", "dict", "字典"), ("key", "string", "键")],
         ret=("string", "键对应的值（不存在返回空串）"),
         desc="按键取值。",
         example='let v = hashmap_get(m, "k");'),
    dict(name="hashmap_contains", cat="哈希表", params=[("map", "dict", "字典"), ("key", "string", "键")],
         ret=("int", "存在为 1，否则 0"),
         desc="判断键是否存在。",
         example='if (hashmap_contains(m, "k") == 1) { }'),
    dict(name="hashmap_remove", cat="哈希表", params=[("map", "dict", "字典"), ("key", "string", "键")],
         ret=("int", "成功为 0"),
         desc="移除键值对。",
         example='hashmap_remove(m, "k");'),
    dict(name="hashmap_size", cat="哈希表", params=[("map", "dict", "字典")],
         ret=("int", "键值对数量"),
         desc="返回字典大小。",
         example='let n = hashmap_size(m);'),
    dict(name="hashmap_free", cat="哈希表", params=[("map", "dict", "字典")],
         ret=("int", "成功为 0"),
         desc="释放字典占用的内存。",
         example='hashmap_free(m);'),

    # 集合（set）
    dict(name="set_new", cat="集合", params=[],
         ret=("set", "空集合（元素为字符串）"),
         desc="创建一个空集合。",
         example='let s = set_new();'),
    dict(name="set_add", cat="集合", params=[("set", "set", "集合"), ("value", "string", "元素")],
         ret=("int", "成功为 0"),
         desc="向集合添加元素。",
         example='set_add(s, "x");'),
    dict(name="set_contains", cat="集合", params=[("set", "set", "集合"), ("value", "string", "元素")],
         ret=("int", "存在为 1，否则 0"),
         desc="判断元素是否在集合中。",
         example='if (set_contains(s, "x") == 1) { }'),
    dict(name="set_remove", cat="集合", params=[("set", "set", "集合"), ("value", "string", "元素")],
         ret=("int", "成功为 0"),
         desc="从集合移除元素。",
         example='set_remove(s, "x");'),
    dict(name="set_size", cat="集合", params=[("set", "set", "集合")],
         ret=("int", "元素数量"),
         desc="返回集合大小。",
         example='let n = set_size(s);'),
    dict(name="set_free", cat="集合", params=[("set", "set", "集合")],
         ret=("int", "成功为 0"),
         desc="释放集合占用的内存。",
         example='set_free(s);'),

    # 日期时间
    dict(name="date_to_str", cat="日期时间", params=[("d", "date", "日期")],
         ret=("string", "字符串形式"),
         desc="将 date 转为字符串。",
         example='let s = date_to_str(today());'),
    dict(name="timestamp_to_str", cat="日期时间", params=[("t", "timestamp", "时间戳")],
         ret=("string", "字符串形式"),
         desc="将 timestamp 转为字符串。",
         example='let s = timestamp_to_str(now());'),
    dict(name="nanotimestamp_to_str", cat="日期时间", params=[("t", "nanotimestamp", "纳秒时间戳")],
         ret=("string", "字符串形式"),
         desc="将 nanotimestamp 转为字符串。",
         example='let s = nanotimestamp_to_str(now_ns());'),

    # 压缩 / 哈希
    dict(name="zip_list", cat="压缩 / 哈希", params=[("spk", "string", ".spk 包路径")],
         ret=("string", "分号分隔的条目列表"),
         desc="列出 .spk 包内的条目。",
         example='let items = str_split(zip_list("x.spk"), ";");'),
    dict(name="content_hash", cat="压缩 / 哈希", params=[("path", "string", "文件路径")],
         ret=("string", "十六进制内容哈希"),
         desc="计算文件内容的哈希（十六进制字符串）。",
         example='let h = content_hash("x.spk");'),
    dict(name="zip_pack", cat="压缩 / 哈希", params=[("src_dir", "string", "源目录"), ("out_spk", "string", "输出 .spk 路径")],
         ret=("int", "成功为 0，失败为 -1"),
         desc="将目录打包为 .spk。",
         example='zip_pack("src", "out.spk");'),
    dict(name="zip_unpack", cat="压缩 / 哈希", params=[("spk", "string", ".spk 包路径"), ("out_dir", "string", "解包目标目录")],
         ret=("int", "成功为 0，失败为 -1"),
         desc="将 .spk 包解包到目录。",
         example='zip_unpack("x.spk", "out");'),

    # 解析
    dict(name="parse_int", cat="解析", params=[("s", "string", "数字字符串")],
         ret=("int", "解析出的整数"),
         desc="将字符串解析为 int（失败返回 0）。",
         example='let n = parse_int("42");'),
    dict(name="parse_long", cat="解析", params=[("s", "string", "数字字符串")],
         ret=("long", "解析出的长整数"),
         desc="将字符串解析为 long（失败返回 0）。",
         example='let n = parse_long("9000000000");'),
    dict(name="parse_float", cat="解析", params=[("s", "string", "数字字符串")],
         ret=("double", "解析出的浮点数"),
         desc="将字符串解析为 double（失败返回 0.0）。",
         example='let f = parse_float("3.14");'),
    dict(name="parse_bool", cat="解析", params=[("s", "string", "布尔字符串")],
         ret=("bool", "解析出的布尔值"),
         desc="将 \"true\"/\"false\" 等解析为 bool。",
         example='let b = parse_bool("true");'),
]


def builtin_signature(b):
    if b["params"]:
        ps = ", ".join(p[0] + ": " + p[1] for p in b["params"])
    else:
        ps = ""
    return "%s(%s) -> %s" % (b["name"], ps, b["ret"][0])


# ---- 标准库抽取 -----------------------------------------------------------
SIG_RE = re.compile(r'^pub\s+kimo\s+(\w+)\s*\(([^)]*)\)\s*->\s*([A-Za-z0-9_<>, \t]+?)\s*(?:\{.*)?$')
PARAM_RE = re.compile(r'([A-Za-z_]\w*)\s*:\s*([\w<>,\s]+?)\s*$')


def extract_std():
    pkgs = {}
    if not os.path.isdir(STD_DIR):
        print("WARN: std dir not found:", STD_DIR)
        return pkgs
    for name in sorted(os.listdir(STD_DIR)):
        pkgpath = os.path.join(STD_DIR, name)
        if not os.path.isdir(pkgpath) or name.endswith(".spk"):
            continue
        funcs = []
        for fn in sorted(os.listdir(pkgpath)):
            if not fn.endswith(".shadow"):
                continue
            funcs += parse_shadow_file(os.path.join(pkgpath, fn))
        if funcs:
            pkgs[name] = funcs
    return pkgs


def parse_shadow_file(path):
    out = []
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        lines = f.readlines()
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i].rstrip("\n")
        m = SIG_RE.match(line.strip())
        if m:
            fname = m.group(1)
            raw_params = m.group(2).strip()
            ret = m.group(3).strip()
            params = []
            if raw_params:
                for part in raw_params.split(","):
                    pm = PARAM_RE.match(part.strip())
                    if pm:
                        params.append((pm.group(1), pm.group(2).strip()))
            # 收集前置 // 注释作为说明（跳过装饰性分隔行）
            desc_lines = []
            j = i - 1
            while j >= 0:
                s = lines[j].strip()
                if s.startswith("//"):
                    body = s[2:].strip()
                    if body and not re.match(r'^([=~\-*#])\1{2,}', body):
                        desc_lines.insert(0, body)
                    j -= 1
                else:
                    break
            desc = " ".join(desc_lines).strip()
            out.append(dict(name=fname, params=params, ret=ret, desc=desc,
                            file=os.path.basename(path)))
        i += 1
    return out


# ---- 渲染 ----------------------------------------------------------------
def render_builtin_page(b):
    sig = builtin_signature(b)
    lines = []
    lines.append("---")
    lines.append("layout: doc")
    lines.append('title: "%s"' % b["name"])
    lines.append('summary: "%s · 内置函数"' % b["cat"])
    lines.append("permalink: /api/builtins/%s/" % b["name"])
    lines.append("---")
    lines.append("")
    lines.append("# `%s`" % b["name"])
    lines.append("")
    lines.append("**%s** 内置函数。" % b["cat"])
    lines.append("")
    lines.append(b["desc"])
    lines.append("")
    lines.append("## 函数签名")
    lines.append("")
    lines.append("```shadow")
    lines.append(sig)
    lines.append("```")
    lines.append("")
    lines.append("## 入参")
    lines.append("")
    if b["params"]:
        lines.append("| 参数 | 类型 | 说明 |")
        lines.append("|------|------|------|")
        for pname, ptype, pdesc in b["params"]:
            lines.append("| `%s` | `%s` | %s |" % (pname, ptype, pdesc))
    else:
        lines.append("无参数。")
    lines.append("")
    lines.append("## 出参")
    lines.append("")
    lines.append("- 类型：`%s`" % b["ret"][0])
    lines.append("- 说明：%s" % b["ret"][1])
    lines.append("")
    lines.append("## 示例")
    lines.append("")
    lines.append("```shadow")
    lines.append(b["example"])
    lines.append("```")
    lines.append("")
    return "\n".join(lines)


def render_std_page(pkg, funcs):
    lines = []
    lines.append("---")
    lines.append("layout: doc")
    lines.append('title: "标准库 · %s"' % pkg)
    lines.append('summary: "std.%s 包导出的公开函数。"' % pkg)
    lines.append("permalink: /api/std/%s/" % pkg)
    lines.append("---")
    lines.append("")
    lines.append("# 标准库 · `std.%s`" % pkg)
    lines.append("")
    lines.append("本页列出 `std/%s` 包导出的全部公开函数（`pub kimo`）。" % pkg)
    lines.append("使用前通过 `import std.%s;` 引入，函数以顶层名直接调用。" % pkg)
    lines.append("")
    for fn in funcs:
        ps = ", ".join(p[0] + ": " + p[1] for p in fn["params"])
        sig = "%s(%s) -> %s" % (fn["name"], ps, fn["ret"])
        lines.append("## `%s`" % fn["name"])
        lines.append("")
        if fn["desc"]:
            lines.append(fn["desc"])
            lines.append("")
        lines.append("```shadow")
        lines.append(sig)
        lines.append("```")
        lines.append("")
        if fn["params"]:
            lines.append("**入参**")
            lines.append("")
            lines.append("| 参数 | 类型 |")
            lines.append("|------|------|")
            for pname, ptype in fn["params"]:
                lines.append("| `%s` | `%s` |" % (pname, ptype))
            lines.append("")
        lines.append("**出参**：`%s`" % fn["ret"])
        lines.append("")
    return "\n".join(lines)


def render_index(builtins, pkgs):
    # 按类别分组内置函数
    cats = {}
    for b in builtins:
        cats.setdefault(b["cat"], []).append(b)
    cat_order = ["输出", "类型转换", "数组", "字符串处理", "文件", "目录 / 路径",
                 "哈希表", "集合", "日期时间", "压缩 / 哈希", "解析"]
    # 保证顺序
    ordered_cats = [c for c in cat_order if c in cats] + [c for c in cats if c not in cat_order]

    lines = []
    lines.append("---")
    lines.append("layout: doc")
    lines.append('title: "库参考"')
    lines.append('summary: "shadow 0.5 内置函数与标准库 API。"')
    lines.append("permalink: /api/")
    lines.append("prev: /modules/")
    lines.append("next: /toolchain/")
    lines.append("---")
    lines.append("")
    lines.append("# 库参考")
    lines.append("")
    lines.append("shadow 0.5 的程序可用两类函数：**内置函数**（由编译器直接提供、无需 import）与 **标准库**（`std.*` 包，需 `import`）。")
    lines.append("")
    lines.append("## 内置函数")
    lines.append("")
    lines.append("内置函数由编译器内建，调用前无需声明或导入。按类别列出：")
    lines.append("")
    for cat in ordered_cats:
        lines.append("### %s" % cat)
        lines.append("")
        lines.append("| 函数 | 签名 | 返回 |")
        lines.append("|------|------|------|")
        for b in cats[cat]:
            sig = builtin_signature(b)
            lines.append("| [`%s`](/api/builtins/%s/) | `%s` | `%s` |" % (b["name"], b["name"], sig, b["ret"][0]))
        lines.append("")
    lines.append("## 标准库")
    lines.append("")
    lines.append("标准库按包组织，使用 `import std.<pkg>;` 引入后，函数以顶层名调用。")
    lines.append("")
    lines.append("| 包 | 说明 | 函数数 |")
    lines.append("|----|------|--------|")
    pkg_desc = {
        "base64": "Base64 / Hex 编解码",
        "collections": "集合、数组与常用算法",
        "http": "HTTP 客户端",
        "https": "HTTPS 客户端",
        "json": "JSON 解析与构造",
        "logging": "日志输出",
        "net": "网络（TCP / UDP）",
        "reflect": "反射与元信息",
        "testkit": "测试框架",
    }
    for pkg in sorted(pkgs.keys()):
        lines.append("| [`std.%s`](/api/std/%s/) | %s | %d |" % (pkg, pkg, pkg_desc.get(pkg, ""), len(pkgs[pkg])))
    lines.append("")
    return "\n".join(lines)


def main():
    os.makedirs(os.path.join(OUT, "builtins"), exist_ok=True)
    os.makedirs(os.path.join(OUT, "std"), exist_ok=True)

    builtins = BUILTINS
    pkgs = extract_std()

    # 内置函数页
    for b in builtins:
        text = render_builtin_page(b)
        with open(os.path.join(OUT, "builtins", b["name"] + ".md"), "w", encoding="utf-8") as f:
            f.write(text)

    # 标准库页
    for pkg, funcs in pkgs.items():
        text = render_std_page(pkg, funcs)
        with open(os.path.join(OUT, "std", pkg + ".md"), "w", encoding="utf-8") as f:
            f.write(text)

    # 总览
    text = render_index(builtins, pkgs)
    with open(os.path.join(OUT, "index.md"), "w", encoding="utf-8") as f:
        f.write(text)

    print("generated: %d builtins, %d std packages (%d functions), index"
          % (len(builtins), len(pkgs), sum(len(v) for v in pkgs.values())))


if __name__ == "__main__":
    main()
