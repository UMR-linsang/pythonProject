sensitive_character = ['你好','小样']     # 敏感词库
test_sentence = input('请输入一段话:')
for line in sensitive_character:     # 遍历输入的字符是存在敏感词库中
    if line in test_sentence:     # 判断是否包含敏感词
        test_sentence = test_sentence.replace(line, '*'*len(line))
print(test_sentence)
