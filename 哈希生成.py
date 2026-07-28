import hashlib

def hash_string(input_string: str, algorithm: str = 'sha256') -> str:
    """
    对输入的字符串计算哈希值，支持多种算法。

    :param input_string: 要哈希的字符串
    :param algorithm: 哈希算法名称，可选值包括 hashlib 支持的所有算法
                      （如 'md5', 'sha1', 'sha256', 'sha512' 等）
    :return: 十六进制格式的哈希字符串
    :raises ValueError: 如果算法不支持或无效
    """
    try:
        # 创建哈希对象
        hash_obj = hashlib.new(algorithm)
        # 更新哈希内容（字符串需编码为字节）
        hash_obj.update(input_string.encode('utf-8'))
        # 返回十六进制摘要
        return hash_obj.hexdigest()
    except ValueError as e:
        raise ValueError(f"不支持的哈希算法 '{algorithm}'，可用算法: {hashlib.algorithms_guaranteed}") from e

# 示例用法
if __name__ == "__main__":
    text = "桜小路ルナ"
    print("MD5:", hash_string(text, "md5"))
    print("SHA-1:", hash_string(text, "sha1"))
    print("SHA-256:", hash_string(text, "sha256"))
    print("SHA-512:", hash_string(text, "sha512"))
    
