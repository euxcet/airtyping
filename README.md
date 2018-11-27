## Air Typing

### Feature
**支持两种手势：**
1. 整个手掌按压完成一次按键，输入一个字符
2. 右手左滑删除，删除末尾字符

**算法：**
每个单词的第一次字符根据按压位置进行概率计算，之后的字符根据和前一个字符的相对位置进行概率计
算。

计算概率时考虑了词频。

坐标系以键盘左上角作为原点，按键大小作为单位长度。

### Todo
**增加手势：**
1. 空格和回车输入手势
2. 删除正在输入的整个单词
3. 双手手势

**算法优化：**
1. 二元词模型
2. 调整词频和按压位置的权重

**UI：**
1. 输入框
2. 按压单词的第一个字符时显示手在键盘上的位置帮助定位
3. 实现真正输入法的效果，在任意可输入位置显示悬浮框
