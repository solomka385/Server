import itertools
class Data():
    def __init__(self,data,IP):
        self.IP = IP
        self.data = data
        
class Server(object):
    newid = itertools.count()
    def __init__(self):
        self.buffer = []
        self.IP = next(self.newid)
    def send_data(self,Data):
        
        self.buffer.append([Data.IP,Data.data])
        
        
    def get_ip(self):
        return self.IP 
    def get_data(self):
        return self.buffer
    
    
class Router(Server):
    newid_r = itertools.count()
    def __init__(self):
        self.soedin = {}
        self.ip = next(self.newid_r)
        self.buffer = []
        super().__init__()
    def link(self,Server):
        self.soedin[Server] = self.ip
       # self.buffer.append(Server.buffer)
    def unlink(self,Server):
        del self.soedin[Server]
    def send_data(self):
        spisok_keys = list(self.soedin)
        for i in spisok_keys:
            self.buffer.append(i.buffer)
        for i in spisok_keys:
            i.buffer = []
        for i in self.buffer:
            for j in i:
                for names in spisok_keys:
                    if names.IP == j[0]:
                        names.buffer.append(j[1])
        
        

  #  def get_link(self):
  #      print(self.soedin)
    

        
router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
#router.get_link()

sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from.send_data(Data("Heo", sv_to.get_ip()))
sv_from.send_data(Data("Helo", sv_to.get_ip()))
sv_from.send_data(Data("Hlo", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
print('fefe')  
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()
print(msg_lst_from)
print(msg_lst_to)