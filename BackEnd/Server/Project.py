import os

def FindRoot(route:str):
    try:
        parent_dir = os.path.dirname(os.path.abspath(route))
        if os.path.exists(os.path.join(route, '.PROJECT_ROOT')):
            return os.path.abspath(route)
        else:
            FindRoot(parent_dir)
    except Exception as e:
        return None
    
def Route(json:str, name:str):
    try:
        table = eval(json)
        return table[name]
    except Exception as e:
        return None