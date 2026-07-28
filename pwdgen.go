package main

import (
	"crypto/rand"
	"fmt"
	"strconv"
	"strings"
)

// 字符集定义
const (
	lowercase = "abcdefghijklmnopqrstuvwxyz"
	uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	digits    = "0123456789"
	specials  = "!@#$%^&*()-_=+[]{}<>?/|~"
)

func main() {
	fmt.Println("=== 密码生成器 ===")

	// 输入密码数量
	count := getPositiveInt("请输入要生成的密码数量: ")

	// 密码长度固定为16
	length := 16

	// 输入是否包含特殊字符
	special := getYesNo("是否包含特殊字符？(y/n): ")

	// 构建字符集
	charset := lowercase + uppercase + digits
	if special {
		charset += specials
	}

	// 生成并输出密码
	fmt.Println("\n生成的密码如下：")
	for i := 0; i < count; i++ {
		pwd, err := generatePassword(length, charset)
		if err != nil {
			fmt.Printf("生成密码失败: %v\n", err)
			return
		}
		fmt.Println(pwd)
	}

	// 等待用户按键退出，防止控制台立即关闭
	fmt.Println("\n按回车键退出...")
	fmt.Scanln()
}

// getPositiveInt 提示用户输入一个正整数，并返回该整数
func getPositiveInt(prompt string) int {
	for {
		fmt.Print(prompt)
		var input string
		fmt.Scanln(&input)
		input = strings.TrimSpace(input)
		num, err := strconv.Atoi(input)
		if err != nil || num <= 0 {
			fmt.Println("输入无效，请输入一个大于0的整数。")
			continue
		}
		return num
	}
}

// getYesNo 提示用户输入 y 或 n，返回对应的布尔值
func getYesNo(prompt string) bool {
	for {
		fmt.Print(prompt)
		var input string
		fmt.Scanln(&input)
		input = strings.ToLower(strings.TrimSpace(input))
		if input == "y" || input == "yes" {
			return true
		} else if input == "n" || input == "no" {
			return false
		} else {
			fmt.Println("输入无效，请输入 y 或 n。")
		}
	}
}

// generatePassword 生成指定长度的随机密码
// 使用 crypto/rand 获取随机字节，并通过拒绝采样确保均匀分布
func generatePassword(length int, charset string) (string, error) {
	charsetLen := len(charset)
	if charsetLen == 0 {
		return "", fmt.Errorf("字符集为空")
	}

	// 计算最大可接受值（小于 256 且为 charsetLen 的倍数），用于拒绝采样
	maxValid := 256 - (256 % charsetLen)

	// 预分配字节切片存储结果
	result := make([]byte, length)

	// 随机数缓冲区
	buf := make([]byte, length)
	for i := 0; i < length; i++ {
		// 循环直到获得一个有效的随机索引
		for {
			// 读取一个随机字节
			_, err := rand.Read(buf[i : i+1])
			if err != nil {
				return "", err
			}

			// 如果值小于 maxValid，则取模后使用
			if b := buf[i]; b < byte(maxValid) {
				result[i] = charset[b%byte(charsetLen)]
				break
			}
			// 否则丢弃并重试
		}
	}

	return string(result), nil
}