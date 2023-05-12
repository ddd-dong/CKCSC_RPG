class Receive_and_update_progress:
    def __init__(self):
  
      
        #各組最新進度
        self.team0_new_progress={'ㄎㄎ長線':{"event":1,"choise":0}, '兇靈線':{"event":1,"choise":0}, '大學長線':{"event":1,"choise":0}, '巫師線':{"event":1,"choise":0}, '李日凱線':{"event":1,"choise":0}}
        self.team1_new_progress={'ㄎㄎ長線':{"event":1,"choise":0}, '兇靈線':{"event":1,"choise":0}, '大學長線':{"event":1,"choise":0}, '巫師線':{"event":1,"choise":0}, '李日凱線':{"event":1,"choise":0}}
        self.team2_new_progress={'ㄎㄎ長線':{"event":1,"choise":0}, '兇靈線':{"event":1,"choise":0}, '大學長線':{"event":1,"choise":0}, '巫師線':{"event":1,"choise":0}, '李日凱線':{"event":1,"choise":0}}
        
        #各組所有經過的節點
        self.team0_all_progress={

                                    '兇靈線':[],
                                    'ㄎㄎ長線':[],
                                    '大學長線':[],
                                    '李日凱線':[],
                                    '巫師線':[]
                                    
                                }
        self.team1_all_progress={

                                    '兇靈線':[],
                                    'ㄎㄎ長線':[],
                                    '大學長線':[],
                                    '李日凱線':[],
                                    '巫師線':[]
                                    
                                }
        self.team2_all_progress={

                                    '兇靈線':[],
                                    'ㄎㄎ長線':[],
                                    '大學長線':[],
                                    '李日凱線':[],
                                    '巫師線':[]
                                    
                                }
    #得到各組進度
    def get_progress(self,team_num):
        #表示要查哪隊-->team_num
        if team_num==0:
            return self.team0_new_progress
        elif team_num==1:
            return self.team1_new_progress
        elif team_num==2:
            return self.team2_new_progress
        

    #得到各組所經歷的進度
    def get_all_progress(self,team_num):
        #表示要查哪隊-->team_num
        if team_num==0:
            return self.team0_all_progress
        elif team_num==1:
            return self.team1_all_progress
        elif team_num==2:
            return self.team2_all_progress
        
    def join(self,team_num,modified_progress,which_plot):
        if team_num==0:
            if which_plot=="兇靈線":
                if modified_progress not in self.team0_all_progress['兇靈線']:
                    self.team0_all_progress['兇靈線'].append(modified_progress)
                    self.team0_new_progress["兇靈線"]=modified_progress

            elif which_plot=="ㄎㄎ長線":
                if modified_progress not in self.team0_all_progress["ㄎㄎ長線"]:
                    self.team0_all_progress['ㄎㄎ長線'].append(modified_progress)
                    self.team0_new_progress["ㄎㄎ長線"]=modified_progress
            elif which_plot=="大學長線":
                if modified_progress not in self.team0_all_progress["大學長線"]:
                    self.team0_all_progress['大學長線'].append(modified_progress)
                    self.team0_new_progress["大學長線"]=modified_progress
            elif which_plot=="李日凱線":
                if modified_progress not in self.team0_all_progress["李日凱線"]:
                    self.team0_all_progress['李日凱線'].append(modified_progress)
                    self.team0_new_progress["李日凱線"]=modified_progress
            elif which_plot=="巫師線":
                if modified_progress not in self.team0_all_progress["巫師線"]:
                    self.team0_all_progress['巫師線'].append(modified_progress)
                    self.team0_new_progress["巫師線"]=modified_progress

        elif team_num==1:
            if which_plot=="兇靈線":
                if modified_progress not in self.team1_all_progress['兇靈線']:
                    self.team1_all_progress['兇靈線'].append(modified_progress)
                    self.team1_new_progress["兇靈線"]=modified_progress
            elif which_plot=="ㄎㄎ長線":
                if modified_progress not in self.team1_all_progress["ㄎㄎ長線"]:
                    self.team1_all_progress['ㄎㄎ長線'].append(modified_progress)
                    self.team1_new_progress["ㄎㄎ長線"]=modified_progress
            elif which_plot=="大學長線":
                if modified_progress not in self.team1_all_progress["大學長線"]:
                    self.team1_all_progress['大學長線'].append(modified_progress)
                    self.team1_new_progress["大學長線"]=modified_progress
            elif which_plot=="李日凱線":
                if modified_progress not in self.team1_all_progress["李日凱線"]:
                    self.team1_all_progress['李日凱線'].append(modified_progress)
                    self.team1_new_progress["李日凱線"]=modified_progress
            elif which_plot=="巫師線":
                if modified_progress not in self.team1_all_progress["巫師線"]:
                    self.team1_all_progress['巫師線'].append(modified_progress)
                    self.team1_new_progress["巫師線"]=modified_progress
                    
        elif team_num==2:
            if which_plot=="兇靈線":
                if modified_progress not in self.team2_all_progress['兇靈線']:
                    self.team2_all_progress['兇靈線'].append(modified_progress)
                    self.team2_new_progress["兇靈線"]=modified_progress
            elif which_plot=="ㄎㄎ長線":
                if modified_progress not in self.team2_all_progress["ㄎㄎ長線"]:
                    self.team2_all_progress['ㄎㄎ長線'].append(modified_progress)
                    self.team2_new_progress["ㄎㄎ長線"]=modified_progress
            elif which_plot=="大學長線":
                if modified_progress not in self.team2_all_progress["大學長線"]:
                    self.team2_all_progress['大學長線'].append(modified_progress)
                    self.team2_new_progress["大學長線"]=modified_progress
            elif which_plot=="李日凱線":
                if modified_progress not in self.team2_all_progress["李日凱線"]:
                    self.team2_all_progress['李日凱線'].append(modified_progress)
                    self.team2_new_progress["李日凱線"]=modified_progress
            elif which_plot=="巫師線":
                if modified_progress not in self.team2_all_progress["巫師線"]:
                    self.team2_all_progress['巫師線'].append(modified_progress)
                    self.team2_new_progress["巫師線"]=modified_progress

        
    def delete(self,team_num,modified_progress,which_plot):

        if team_num==0:
            if which_plot=="兇靈線":
                if modified_progress in self.team0_all_progress['兇靈線']:

                    ind=self.team0_all_progress['兇靈線'].index(modified_progress)
                    self.team0_all_progress['兇靈線'].pop(ind)
                   

            elif which_plot=="ㄎㄎ長線":
                if modified_progress in self.team0_all_progress["ㄎㄎ長線"]:

                    
                    self.team0_all_progress['ㄎㄎ長線'].remove(modified_progress)

            elif which_plot=="大學長線":
                if modified_progress in self.team0_all_progress["大學長線"]:
                    
                
                    self.team0_all_progress['大學長線'].remove(modified_progress)

            elif which_plot=="李日凱線":
                if modified_progress in self.team0_all_progress["李日凱線"]:

 
                    self.team0_all_progress['李日凱線'].remove(modified_progress)

            elif which_plot=="巫師線":
                if modified_progress in self.team0_all_progress["巫師線"]:

 
                    self.team0_all_progress['巫師線'].remove(modified_progress)

        elif team_num==1:
            if which_plot=="兇靈線":
                if modified_progress in self.team1_all_progress['兇靈線']:
                    self.team1_all_progress['兇靈線'].remove(modified_progress)
            elif which_plot=="ㄎㄎ長線":
                if modified_progress in self.team1_all_progress["ㄎㄎ長線"]:
                    self.team1_all_progress['ㄎㄎ長線'].remove(modified_progress)
            elif which_plot=="大學長線":
                if modified_progress in self.team1_all_progress["大學長線"]:
                    self.team1_all_progress['大學長線'].remove(modified_progress)
            elif which_plot=="李日凱線":
                if modified_progress in self.team1_all_progress["李日凱線"]:
                    self.team1_all_progress['李日凱線'].remove(modified_progress)
            elif which_plot=="巫師線":
                if modified_progress in self.team1_all_progress["巫師線"]:
                    self.team1_all_progress['巫師線'].remove(modified_progress)
                    
        elif team_num==2:
            if which_plot=="兇靈線":
                if modified_progress in self.team2_all_progress['兇靈線']:
                    self.team2_all_progress['兇靈線'].remove(modified_progress)
            elif which_plot=="ㄎㄎ長線":
                if modified_progress in self.team2_all_progress["ㄎㄎ長線"]:
                    self.team2_all_progress['ㄎㄎ長線'].remove(modified_progress)
            elif which_plot=="大學長線":
                if modified_progress in self.team2_all_progress["大學長線"]:
                    self.team2_all_progress['大學長線'].remove(modified_progress)
            elif which_plot=="李日凱線":
                if modified_progress in self.team2_all_progress["李日凱線"]:
                    self.team2_all_progress['李日凱線'].remove(modified_progress)
            elif which_plot=="巫師線":
                if modified_progress in self.team2_all_progress["巫師線"]:
                    self.team2_all_progress['巫師線'].remove(modified_progress)        
    
        
    def update_team_progress(self,team_num:int,delete_or_join:str,modified_progress:dict,
which_plot:str):
        #表示要修改哪隊-->team_num
        
    
        if team_num==0:

            if delete_or_join=="delete":
                self.team0_progress=self.delete(team_num,modified_progress,which_plot)
            elif delete_or_join=="join":
                self.team0_progress=self.join(team_num,modified_progress,which_plot)

        elif team_num==1:

            if delete_or_join=="delete":
                self.team1_progress=self.delete(team_num,modified_progress,which_plot)
            elif delete_or_join=="join":
                self.team1_progress=self.join(team_num,modified_progress,which_plot)

        elif team_num==2:
            if delete_or_join=="delete":
                self.team2_progress=self.delete(team_num,modified_progress,which_plot)
            elif delete_or_join=="join":
                self.team2_progress=self.join(team_num,modified_progress,which_plot)


#get_progress使用
progress_tracker = Receive_and_update_progress()
# print(progress_tracker.get_all_progress(0))
# print(progress_tracker.get_progress(0))
# progress_tracker.update_team_progress(1,"join",{"event":1,"choise":0},"兇靈線")
# progress_tracker.update_team_progress(0,"join",{"event":1,"choise":1},"兇靈線")
# print(progress_tracker.get_progress(0))
# progress_tracker.update_team_progress(0,"delete",{"event":1,"choise":1},"兇靈線")
# progress_tracker.update_team_progress(1,"delete",{"event":1,"choise":0},"兇靈線")
# print(progress_tracker.get_all_progress(0))
# print(progress_tracker.get_all_progress(1))
