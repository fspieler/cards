#/usr/bin/env python3

class User(object):
    def __init__(self,user_id=None):
        if user_id == None:
            self.new_user = True
            user_id = time.time()
        else:
            self.new_user = False
            #fetch all records from db about user_id
            self._populateUser() 

    def commit(self):
        if self.new_user:
            pass
        else:
            #Do UPDATES 
            pass

    def hole_cards():
        # fetch cards for user_id
        pass

    def delete(self):
        if self.new_user == False:
            return False
            # Delete user code here
