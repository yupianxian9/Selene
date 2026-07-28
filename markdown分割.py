import os
import re
from pathlib import Path

def split_markdown_by_h1():
    """
    按一级标题分割Markdown文件并生成目录索引页
    参数直接在代码中设置
    """
    # ========== 在这里设置参数 ==========
    input_file = "求职笔记.md"        # 输入的Markdown文件路径
    output_dir = "output"          # 输出目录
    # ===================================
    
    # 检查输入文件是否存在
    if not os.path.exists(input_file):
        print(f"错误：输入文件 {input_file} 不存在")
        return False

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"读取文件时出错: {e}")
        return False

    # 创建输出目录
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # 提取元数据（如YAML front matter）
    def extract_metadata(content):
        metadata = {}
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) > 2:
                metadata_str = parts[1]
                content = parts[2].lstrip()
                # 简易YAML解析（基础键值对）
                for line in metadata_str.split('\n'):
                    if ':' in line:
                        key, value = line.split(':', 1)
                        metadata[key.strip()] = value.strip().strip('\"\'')
        return metadata, content

    def sanitize_filename(title):
        """将标题转换为安全的文件名"""
        # 移除非允许字符，替换空格和减号
        title = re.sub(r'[^\w\s-]', '', title).strip()
        title = re.sub(r'[-\s]+', '-', title)
        return title.lower()

    metadata, content = extract_metadata(content)

    # 正则表达式匹配一级标题（格式: # 标题）
    h1_pattern = re.compile(r'^#\s+(.+)$', re.MULTILINE)

    # 查找所有一级标题的位置
    matches = list(h1_pattern.finditer(content))
    if not matches:
        print("未找到一级标题，文件将不会被分割")
        return False

    # 收集所有分段（包括前言和各个一级标题部分）
    sections = []
    current_pos = 0

    # 处理第一个标题前的内容（前言）
    if matches[0].start() > current_pos:
        preamble = content[current_pos:matches[0].start()].strip()
        if preamble:  # 只有前言非空时才添加
            sections.append(('前言', preamble))

    # 处理每个一级标题部分
    for i, match in enumerate(matches):
        title = match.group(1)
        # 当前标题的起始位置
        start_idx = match.start()
        # 当前标题的结束位置（下一个标题之前或文件末尾）
        end_idx = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        section_content = content[start_idx:end_idx].strip()
        sections.append((title, section_content))

    # 生成目录索引页内容
    toc_lines = []
    # 如果有元数据，先写入元数据
    toc_content = "---\n" if metadata else ""
    for key, value in metadata.items():
        toc_content += f"{key}: {value}\n"
    if metadata:
        toc_content += "---\n\n"
    toc_content += "# 目录\n\n"

    # 构建目录列表并写入各分割文件
    file_list = []
    for i, (title, section_content) in enumerate(sections):
        if title == '前言':
            filename = "00-preamble.md"
            toc_line = f"- [{title}]({filename})"
        else:
            safe_title = sanitize_filename(title)
            filename = f"{i:02d}-{safe_title}.md"
            toc_line = f"- [{title}]({filename})"
        
        toc_lines.append(toc_line)
        file_list.append(filename)

        # 为每个分割文件添加元数据（仅第一个文件添加完整元数据）
        file_header = ""
        if i == 0 and metadata:
            file_header = "---\n"
            for key, value in metadata.items():
                file_header += f"{key}: {value}\n"
            file_header += "---\n\n"

        # 写入分割后的文件
        file_path = os.path.join(output_dir, filename)
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(file_header + section_content)
            print(f"已生成: {filename}")
        except Exception as e:
            print(f"写入文件 {filename} 时出错: {e}")
            return False

    # 完成目录索引页内容
    toc_content += "\n".join(toc_lines)

    # 写入目录索引页（README.md）
    toc_path = os.path.join(output_dir, "README.md")
    try:
        with open(toc_path, 'w', encoding='utf-8') as f:
            f.write(toc_content)
        print(f"目录索引页已生成: {toc_path}")
    except Exception as e:
        print(f"写入目录索引页时出错: {e}")
        return False

    print(f"\n分割完成！共生成 {len(sections)} 个文件到目录: {output_dir}")
    return True

def main():
    """主函数"""
    print("开始分割Markdown文件...")
    print("=" * 50)
    
    success = split_markdown_by_h1()
    
    print("=" * 50)
    if success:
        print("分割操作成功完成！")
    else:
        print("分割操作失败！")

if __name__ == "__main__":
    main()