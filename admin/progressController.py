from __init__ import teamNumber,list_of_lines,possible_next
#格式為 如果為單線  直接放下一格
#如果為選擇 [0] = 'other' [1] = 'choose one' [2] = list of choices
#如果為無序多任務 [0]='other' [1] = 'unordered' [2] = todo list [3] = next (after mutiroads)
#len為最常不含0之路徑
class create_progress:
    def __init__(self) :
        self.new_progress = {
                                '自殺案':  '1-0',
                                '債主案':'1-0',
                                '歌妓案':'1-0',
                                '劍客案':'1-0',
                                '鐵匠線':  '1-0',
                                '主線':  '1-0'
                            }
        self.all_progress = {
                                '自殺案':       ['1-0'],
                                '債主案':     ['1-0'],
                                '歌妓案':     ['1-0'],
                                '劍客案':     ['1-0'],
                                '鐵匠線':       ['1-0'] ,
                                '主線':       ['1-0']      
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
            done = len(self.get_self_team_all_progress(team_num)[line])
            # present = f'line \'{line}\' done{done/(all-1)*100}%'
            s[line] = int(done/(all)*100)
            # s.append(present)
        return s
    
    #加入 (隊伍,哪條線,薪點)
    def join(self, team_num:int, modified_road:str, line:str):

        new = self.get_self_team_new_progress(team_num)
        now = new[line]
        next = possible_next[line][now][0]
        

        # if possible_next[line][now][1] == 'judge':
            # return self.join(team_num, next, line)
        #aaaaaaaa
        if next == 'end':
            return 'This road has already end!!!!!!!!!!!'

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
            elif possible_next[line][now][1] != 'doing':
                if modified_road in possible_next[line][now][2]:
                    next = modified_road
                possible_next[line]['ender'] = possible_next[line][now][1]

            
            
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
            self.teams[team_num].new_progress[line] = modified_road
            next = possible_next[line][modified_road][0]
            try :
                if (possible_next[line][modified_road][1]) == 'judge' :
                    jump = modified_road.split('-')[0]
                    return self.join(team_num,f'{jump}-{possible_next[line]["ender"]}',line)
            except:
                pass
            if next == 'end' :
                return f"HOORAY!!! you finish road {line}"
            return f'Success push \'{modified_road}\' into line {line}'
        
        else :
            if next == 'other' :
                return f'You try to push \n\'{modified_road}\'\n but the possilbe nexts are {possible_next[line][now][2]}'
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

# print(a.join(3,'2-0','兇靈線'))
# print(a.join(3,'3-0','兇靈線'))
# print(a.join(3,'4-0','兇靈線'))
# print(a.join(3,'5-0','兇靈線'))
# print(a.join(3,'6-0','兇靈線'))
# print(a.get_self_team_new_progress(3))
# print(a.join(3,'7-2','兇靈線'))
# print(a.join(3,'8-0','兇靈線'))
# print(a.join(3,'9-0','兇靈線'))
# print(a.join(3,'10-0','兇靈線'))
# print(a.join(3,'11-0','兇靈線'))
# print(a.join(3,'12-0','兇靈線'))
# print(a.join(3,'13-0','兇靈線'))
# print(a.join(3,'14-0','兇靈線'))
# print(a.join(3,'14-1','兇靈線'))
# print(a.get_self_team_new_progress(3))
# print(a.join(3,'14-2','兇靈線'))
# print(a.join(3,'14-3','兇靈線'))
# print(a.join(3,'15-0','兇靈線'))

# print(a.get_self_team_all_progress(3))
# print(possible_next['兇靈線']['ender'])

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
# print(a.join(3,'2-0','主線'))
# print(a.join(3,'3-0','主線'))
# print(a.join(3,'4-0','主線'))
# print(a.join(3,'5-0','主線'))
# print(a.join(3,'6-0','主線'))
# print(a.join(3,'7-0','主線'))
# print(a.join(3,'8-1','主線'))
# print(a.join(3,'8-0','主線'))
# print(a.join(3,'8-2','主線'))
# print(a.join(3,'8-1','主線'))
# print(a.join(3,'9-0','主線'))
# print(a.join(3,'10-0','主線'))
# print(a.get_self_team_new_progress(3))
# print(a.join(3,'11-0','主線'))
# print(a.get_self_team_all_progress(3))
# print(a.join(3,'11-2','主線'))
