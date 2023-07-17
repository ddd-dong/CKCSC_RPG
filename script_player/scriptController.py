import json
import copy
from __init__ import index_path,list_of_lines as lines

# line是指哪故事線


role_list = ['旁白', '莫塞伊思', '關主', '檢測人員',"鐵匠",""]
roles = []


class Role:
    """
    name 角色名稱
    appear 角色出現在那些地方
    show 角色出現的事件數量
    """
    def __init__(self, name):
        self.name = name
        self.appear = {}
        self.show = 0

    def add_event(self, event):
        # print()
        # print(event)
        # print(self.name)
        # print()
        if self.appear.get(event.line) is None:
            self.appear[event.line] = []
        self.appear[event.line].append(event)
        self.show += 1


class Event:
    """
    act 此事件在第幾階段
    line 此事件在哪個故事線
    end bool 是否是劇終
    compendium 這事件的概要，對應notion的劇情
	role 角色，對應notion的角色
	text 台詞，對應notion的台詞
	key 觸發條件
	item 道具
    """
    def __init__(self, awa, num, line):
        self.act: int = num
        self.line: str = line
        self.end: bool = awa['end']
        self.compendium: str = awa['com']
        self.role: str = awa['role']
        self.text: str = awa['text']
        self.key: str = awa['key']
        self.item: str = awa['item']

    def to_dict(self):
        temp = {}
        temp['end'] = self.end
        temp['com'] = self.compendium
        temp['role'] = self.role
        temp['text'] = self.text
        temp['key'] = self.key
        temp['item'] = self.item
        return temp


class Task:
    """
    description 這類型的意義
    """
    def __init__(self):
        self.type = "Task"
        self.description = "代表這是一個單純對話的階段，不會有選項或子事件"


class Choose:
    """
    description 這類型的意義
    opt 選項
    """
    def __init__(self, opt):
        self.type = "Choose"
        self.description = "代表這是一個有選項的階段，會有選項影響玩家會到的子事件"
        self.opt = opt


class Multiple:
    """
    description 這類型的意義
    events 子事件數量
    detail 怎樣的分支
        'route' 代表劇情岔路
        'collect' 代表要收集某些事物
    """
    def __init__(self, events: int, types: str):
        self.type = "Multiple"
        self.description = "代表這個階段會有子事件，detail會代表是劇情分支還是去收集某些事物"
        self.events = events
        self.detail = types


class Act:
    """
    num 代表第幾階段
    line 在哪個故事線
    types 階段類型
    data 建構時用來給資料
    event 此階段的事件，呼叫事件請使用get_event()
    """

    def who(self, name):
        """
        coco ㄎㄎ長 0
        ghost 兇靈 1
        senior 大學長 2
        wizard 巫師 3
        rekai 李日凱 4
        """
        if name == "旁白":
            return roles[0]
        elif name == "莫塞伊思":
            return roles[1]
        elif name == "關主":
            return roles[2]
        elif name == "檢測人員":
            return roles[3]
        elif name == "鐵匠":
            return roles[4]
        elif name == "":
            return roles[5]

    def __init__(self, num: int, line: str, types: str, data: dict):
        self.num = num
        self.line = line
        self.data = data
        if types == "multiple":
            temp = []
            self.type = Multiple(events=data['remark'][0], types=data['remark'][1])
            for i in data['event']:
                e = Event(awa=i, num=num, line=line)
                temp.append(e)
                self.who(i['role']).add_event(event=e)
            self.event = temp
        elif types == "choose":
            self.type = Choose(opt=data['remark'])
            e = Event(awa=data['event'][0], num=num, line=line)
            self.event = e
            self.who(data['event'][0]['role']).add_event(event=e)
        elif types == "task":
            self.type = Task()
            e = Event(awa=data['event'][0], num=num, line=line)
            self.event = e
            self.who(data['event'][0]['role']).add_event(event=e)

    def get_event(self, num: int = None):
        if type(self.type) != Multiple and num is None:
            return self.event
        elif type(self.type) == Multiple:
            if num > self.type.events:
                raise f"在呼叫階段子事件時，num參數超出事件數量"
            return self.event[num-1]
        else:
            return self.event

    def to_dict(self):
        return self.data


class StoryLine:
    """
    name 故事線名稱
    len 階段數量
    act 階段list呼叫階段請使用get_act()
    """
    def __init__(self, name: str):
        with open(index_path+f'/RPGscrpit/{name}.json', 'r', encoding='utf8') as jfile:
            data = json.load(jfile)
            self.name = name
            self.len = data['info']['max']
            temp = []
            for i in range(self.len):
                detail = data[str(i + 1)]
                temp.append(Act(num=i+1,
                                line=name,
                                types=detail['type'],
                                data=detail)
                            )
            self.act = temp

    def get_act(self, num: int):
        if num > self.len:
            raise f"在呼叫階段時，num參數超出階段數量"
        return self.act[num-1]

    def get_before(self, num:int):
        if num > self.len:
            raise f"在呼叫階段時，num參數超出階段數量"
        temp = {}
        for a in self.act:
            if a.num > num:
                break
            temp[str(a.num)] = a.data

        return temp


class Roles:
    """
    coco ㄎㄎ長
    ghost 兇靈
    senior 大學長
    wizard 巫師
    rekai 李日凱
    """
    def __init__(self):
        self.coco = Role(name="旁白")
        self.ghost = Role(name="莫塞伊思")
        self.senior = Role(name="關主")
        self.wizard = Role(name="檢測人員")
        self.rekai = Role(name="鐵匠")
        self.emptyr = Role(name="")
        self.pool = [self.coco,
                     self.ghost,
                     self.senior,
                     self.wizard,
                     self.rekai,
                     self.emptyr]
        global roles
        roles = [self.coco,
                     self.ghost,
                     self.senior,
                     self.wizard,
                     self.rekai,
                     self.emptyr]


class Script:
    """
    使用時直接創立這個物件就包含了五個故事線
    roles 角色池物件Roles
    coco ㄎㄎ長線
    ghost 兇靈線
    senior 大學長線
    wizard 巫師線
    rekai 李日凱線
    """
    def __init__(self):
        self.roles = Roles()
        self.coco = StoryLine(name='自殺案')
        self.ghost = StoryLine(name='債主案')
        self.senior = StoryLine(name='歌妓案')
        self.wizard = StoryLine(name='劍客案')
        self.rekai = StoryLine(name='鐵匠線')
        self.mainline = StoryLine(name='主線')




'''
這只是我測試用的 理論上這應該沒問題了吧
我會留下只是給使用者看看我大概的希望他備用的樣子大概長這樣

s = Script()
print(s)
print(s.ghost)
print(s.ghost.get_act(1).type)
print(s.ghost.get_act(7).get_event(1))
print(s.ghost.get_act(7).get_event(2).end)
print(s.ghost.get_act(7).get_event(2).compendium)
print(s.roles.ghost.appear)
print(s.roles.rekai.appear)
a = s.ghost.get_before(8)
print(a)
print(a["7"].type)
print(a["7"].event)
print(a["7"].event.end)
'''
RPG_Full_Script = Script()
# RPG_Script = {'ㄎㄎ長線':, '兇靈線':, '大學長線':, '巫師線':, '李日凱線':RPG_Full_Script.rekai}
RPG_Script ={'自殺案':RPG_Full_Script.coco,'債主案':RPG_Full_Script.ghost,'歌妓案':RPG_Full_Script.senior,'劍客案':RPG_Full_Script.wizard,'鐵匠線':RPG_Full_Script.rekai,'主線':RPG_Full_Script.mainline}

# print(RPG_Script['兇靈線'].get_before(15))
# print(RPG_Script['兇靈線'].get_act(5).get_event(1).act)