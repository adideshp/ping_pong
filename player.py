import random

class Player:
    def __init__(self, name, defense_arr_length):
        self.name = name
        self.defense_arr_length = round(defense_arr_length)

    def get_guess(self, seed = None, _from=0, _to= 10):
        random.seed(seed)
        return random.randint(round(_from), round(_to))
    
    def get_defense_array(self,  _from=0, _to=10):
        ret_list = []
        for i in range(0,self.defense_arr_length):
            ret_list.append(random.randint(round(_from), round(_to)))
        return ret_list
