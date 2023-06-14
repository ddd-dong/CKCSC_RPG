from __init__ import teamNumber,list_of_lines,possible_next

#格式為 如果為單線  直接放下一格
#如果為選擇 [0] = 'other' [1] = 'choose one' [2] = list of choices
#如果為無序多任務 [0]='other' [1] = 'unordered' [2] = todo list [3] = next (after mutiroads)
#len為最常不含0之路徑

class create_progress:
    def __init__(self) :
        self.new_progress = {
                                '兇靈線':  '1-0',
                                'ㄎㄎ長線':'1-0',
                                '大學長線':'1-0',
                                '李日凱線':'1-0',
                                '巫師線':  '1-0'
                            }
        self.all_progress = {
                                '兇靈線':       ['1-0'],
                                'ㄎㄎ長線':     ['1-0'],
                                '大學長線':     ['1-0'],
                                '李日凱線':     ['1-0'],
                                '巫師線':       ['1-0']       
                            }
        
#建立物件時需要輸入隊伍總數

class controller:
    def __init__(self, teamcounts = 3) -> None:
        self.all_teams = teamcounts
        self.teams = []
        self.doing = {}
        # self.lost = []
        self.unorder_running =False
        for i in range(teamcounts):
            x = create_progress()
            self.teams.append(x)

    #最新進度    
    def get_self_team_new_progress(self, team_num)->dict:
        return self.teams[team_num].new_progress
    #全進度
    def get_self_team_all_progress(self, team_num)->dict:
        return self.teams[team_num].all_progress
    
    def get_all_team_new_progress(self) :
        dic = {}
        for i in range(self.all_teams):
            s = f'{i}'
            dic[s] = self.get_self_team_new_progress(i)
        return dic
        
    def get_all_team_all_progress(self):
        dic = {}
        for i in range(self.all_teams):
            s = f'{i}'
            dic[s] = self.get_self_team_all_progress(i)
        return dic

    #完成度
    def total(self, team_num) -> list:
        s = {}
        for line in list_of_lines:
            all = possible_next[line]['len']
            done = len(a.get_self_team_all_progress(team_num)[line])
            # present = f'line \'{line}\' done{done/(all-1)*100}%'
            s[line] = done/(all-1)*100
            # s.append(present)
        return s
    
    #加入 (隊伍,哪條線,薪點)
    def join(self, team_num:int, modified_road:str, line:str):

        new = self.get_self_team_new_progress(team_num)
        now = new[line]
        next = possible_next[line][now][0]
        
        if next == 'end':
            return 'this road has already end'
        
        
        if next == 'other':
            if possible_next[line][now][1] == 'chooce one':
                if modified_road in possible_next[line][now][2]:
                    next = modified_road
            elif possible_next[line][now][1] == 'unordered' :
                self.doing['at'] = now
                self.doing['next'] = possible_next[line][now][3]
                self.doing['todo_list'] = possible_next[line][now][2]
                self.doing['done_list'] = []
                self.unorder_running = True
                if modified_road in self.doing['todo_list']:
                    next = modified_road
            
            
            if self.unorder_running:
                if possible_next[line][now][1] == 'doing':
                    if now not in self.doing['done_list'] and (now in self.doing['todo_list']):
                        self.doing['done_list'].append(now)
                    if modified_road not in self.get_self_team_all_progress(3)[line] and modified_road in self.doing['todo_list']:
                        next = modified_road
                self.doing['done_list'].sort()
                self.doing['todo_list'].sort()
                if self.doing['next'] == modified_road and (self.doing['done_list'] == self.doing['todo_list']):
                    next = modified_road
                    self.unorder_running = False
                    self.doing ={}


        if modified_road == next :  
            self.teams[team_num].all_progress[line].append(modified_road)
            # try :
            #     inx = self.lost.index(modified_road)
            #     self.lost.pop(inx)
            # except:
            #     pass
            self.teams[team_num].new_progress[line] = modified_road
            next = possible_next[line][modified_road][0]
            if next == 'end' :
                return f"HOORAY!!! you finish road {line}"
            return f'success push \'{modified_road}\' into line {line}'
        
        else :
            return f'you try to push \n\'{modified_road}\'\nbut the next is \n\'{next}\'  '
    
    #刪除 (隊伍,哪條線,薪點)
    def delete(self, team_num:int,modified_road:str,line:str):
        new = self.get_self_team_new_progress(team_num)
        now = new[line]
        assert modified_road in self.teams[team_num].all_progress[line]
        assert len(self.teams[team_num].all_progress[line]) > 1
        if modified_road == now:
            self.teams[team_num].all_progress[line].pop()
            self.teams[team_num].new_progress[line]= self.teams[team_num].all_progress[line][len(self.teams[team_num].all_progress[line])-1]
        else :
            ind = self.teams[team_num].all_progress[line].index(modified_road)
            self.teams[team_num].all_progress[line].pop(ind)
            # self.lost.append(modified_road)
    
    #暫不設計警告
    # def warn(self):
    #     if len(self.lost) != 0:
    #         print(self.lost)



"""下方為範例測資可自由測試"""
progress_tracker = controller(teamcounts=teamNumber)
# a =controller(teamcounts=5)

# b = a.get_self_team_new_progress(3)['兇靈線']
# print(possible_next['兇靈線'][b])


# print(a.join(3,'2-0','李日凱線'))
# print(a.get_self_team_all_progress(3))

# print(a.join(3,'李日凱線','7=0'))
# print(a.get_self_team_all_progress(3))

# print(a.join(3,'李日凱線','3-2'))
# print(a.get_self_team_all_progress(3))

# print(a.join(3,'李日凱線','3-2'))
# print(a.get_self_team_all_progress(3))
# print(a.join(3,'李日凱線','3-1'))

# # print(a.delete(3,'李日凱線','2'))
# print(a.get_self_team_all_progress(3))
# print(a.get_self_team_new_progress(3))
# print(a.join(3,'李日凱線','4-0'))
# print(a.get_self_team_all_progress(3))


# print(a.join(3,'李日凱線','3-1'))
# print((a.join(3,'李日凱線','4-0')))
# print((a.join(3,'李日凱線','4-0')))
# print((a.join(3,'李日凱線','5-0')))
# print((a.join(3,'李日凱線','6-0')))
# # print((a.join(3,'李日凱線','7')))
# # print((a.join(3,'李日凱線','8')))
# print((a.join(3,'李日凱線','8-1')))
# print((a.join(3,'李日凱線','8-3')))
# a.join(3,'巫師線','2-0')

# print((a.join(3,'李日凱線','8-2')))
# print((a.join(3,'李日凱線','8-4')))
# print((a.join(3,'李日凱線','9-0')))
# print((a.join(3,'李日凱線','10-0')))
# print((a.join(3,'李日凱線','11-0')))
# print('----------------')
# print(a.get_self_team_all_progress(3))