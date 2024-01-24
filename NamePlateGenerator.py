import json
from datetime import datetime

# =============================================================================
def createnameplate(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        
    required_keys = ['projectname', 'framework', 'modelinfo']  # Replace with your desired keys
    
    if len(data.keys()) != len(required_keys):
        raise ValueError("JSON does not contain the required number of keys.")
    
    assert isinstance(data['projectname'], str), "Projectname should be a string."
    assert isinstance(data['framework'], str), "Framework should be a string."
    
    nameplate = "%s_%s_%s"%(data['projectname'], data['framework'], data['modelinfo'])
    
    current_date = datetime.now().strftime("%b%d_%Y")
#    print(current_date)
    
    nameplate = "%s_%s_"%(nameplate, current_date)
    return nameplate
# =============================================================================

if __name__ == '__main__':
    data = createnameplate('test.json')
    print(data)