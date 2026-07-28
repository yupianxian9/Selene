@echo off
setlocal enabledelayedexpansion
chcp 65001 >nul  & REM 确保控制台支持中文注释显示

REM 定义字符集：大写字母、小写字母、数字
set "upper=ABCDEFGHIJKLMNOPQRSTUVWXYZ"
set "lower=abcdefghijklmnopqrstuvwxyz"
set "digit=0123456789"
set "all_chars=%upper%%lower%%digit%"  & REM 合并所有可用字符（共62个）

REM 设置生成参数：9个密码，每个16位
set /a password_count=9
set /a password_length=16
set /a mandatory_chars=3  & REM 必须先包含的3种字符类型

echo Generating %password_count% random passwords (%password_length% characters each)...
echo.

for /l %%i in (1,1,%password_count%) do (
    set "password="
    
    REM 第一步：先确保包含1位数字、1位大写字母、1位小写字母
    set "temp_password="
    
    REM 生成1位数字
    set /a rand_index=!random! %% 10
    call set "char=%%digit:~!rand_index!,1%%"
    set "temp_password=!temp_password!!char!"
    
    REM 生成1位大写字母
    set /a rand_index=!random! %% 26
    call set "char=%%upper:~!rand_index!,1%%"
    set "temp_password=!temp_password!!char!"
    
    REM 生成1位小写字母
    set /a rand_index=!random! %% 26
    call set "char=%%lower:~!rand_index!,1%%"
    set "temp_password=!temp_password!!char!"
    
    REM 第二步：随机生成剩下的13位字符
    set /a remaining_chars=!password_length! - !mandatory_chars!
    for /l %%j in (1,1,!remaining_chars!) do (
        set /a rand_index=!random! %% 62
        call set "char=%%all_chars:~!rand_index!,1%%"
        set "temp_password=!temp_password!!char!"
    )
    
    REM 第三步：对字符进行随机乱序，增加随机性[4](@ref)
    set "password="
    set "shuffle_source=!temp_password!"
    set /a chars_left=!password_length!
    
    for /l %%k in (1,1,!password_length!) do (
        set /a rand_pos=!random! %% !chars_left!
        call set "selected_char=%%shuffle_source:~!rand_pos!,1%%"
        set "password=!password!!selected_char!"
        
        REM 从源字符串中移除已选字符[4](@ref)
        if !rand_pos! equ 0 (
            set "shuffle_source=!shuffle_source:~1!"
        ) else (
            call set "left_part=%%shuffle_source:~0,!rand_pos!%%"
            set /a next_pos=!rand_pos! + 1
            call set "right_part=%%shuffle_source:~!next_pos!%%"
            set "shuffle_source=!left_part!!right_part!"
        )
        set /a chars_left=!chars_left! - 1
    )
    
    echo Password %%i: !password!
)

echo.
pause  & REM 暂停等待用户操作
exit /b
