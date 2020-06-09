# 创建 Kiana 类（注意：约定类名首字母大写）
class Kiana():
    """创建一个“Kiana”类"""

    def __init__(self, armour, property, rank):
        """初始化属性：name、rank"""
        self.armour = armour
        self.property = property
        self.rank = rank
    
    def info(self):
        """显示装甲信息"""
        print("【角色】琪亚娜·卡斯兰娜")
        print("【装甲】" + self.armour)
        print("【属性】" + self.property)
        print("【星阶】" + self.rank)
        print("\n")

    def normal_attack(self):
        print("【普通攻击】\n")

    def special_attack(self):
        print("【必杀技】\n")


# 实例化
bailian = Kiana("领域装·白练", "机械", "A")
moonlight = Kiana("白骑士·月光", "生物", "S")

# print("琪亚娜的" + moonlight.rank + "级装甲是：" + moonlight.armour)

moonlight.info()
bailian.info()
