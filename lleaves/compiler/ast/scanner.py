"""
The Scanner is responsible for iterating over the model.txt and transforming it into a more
usable representation.
It doesn't implement any transformations (expect for type casting).
"""



def scan_model_file(file_path, features=None):
    res = {"trees": []}
    features = ['Adj_Close', 'Close', 'High', 'Low', 'Open', 'Volume']
    assert features!=None
    num_features = len(features)


    scanned_model_dict = {
    'trees': [],
    'general_info': {
        'features': list,  
        'num_class': int,
        'feature_infos': ['[11.898214340209959:25.181070327758789]']*num_features,  # NEED TO CHANGE 
        'num_tree_per_iteration': int,
        'max_feature_idx': int,
        'objective': ['regression'],
    }}

    model = readfile(file_path)
    model_dict = extract(model)

    # print(len(model_dict), model_dict[1][12])

    scanned_model_dict['general_info']['features'] = features
    scanned_model_dict['general_info']['max_feature_idx'] = len(features)-1
    scanned_model_dict['general_info']['num_tree_per_iteration'] = 1
    scanned_model_dict['general_info']['num_class'] = 1


    #######################################################################
    for tri in range(len(model_dict)):


        tobj  = {
                'Tree': int,
                'num_leaves': int,
                'split_feature': list,
                'threshold': list,
                'decision_type': list,
                'left_child': list,
                'right_child': list,
                'leaf_value': list }
    
        threshold = []
        l =[]
        r =[]
        split_feature = []
        indices = []

        for idx in model_dict[tri]:
            if 'tresh' in model_dict[tri][idx].keys():
                indices.append(idx)
        
        leaves = []
        num_leaves = 0
        tidx = []
        lidx = []
        
        for idx in range(len(model_dict[tri])):
            if 'tresh' in model_dict[tri][idx].keys():
                tidx.append(idx)
            else:
                lidx.append(idx)

        for idx in range(len(model_dict[tri])):
            # print(tri,idx)
            if 'tresh' in model_dict[tri][idx].keys():
                threshold.append(model_dict[tri][idx]['tresh'])
                split_feature.append(model_dict[tri][idx]['index'])
                
                if 'leaf' in model_dict[tri][model_dict[tri][idx]['yes']]:
                    l.append(-1*(lidx.index(model_dict[tri][idx]['yes'])+1))
                else:
                    l.append(tidx.index(model_dict[tri][idx]['yes']))
                
                if 'leaf' in model_dict[tri][model_dict[tri][idx]['no']]:
                    r.append(-1*(lidx.index(model_dict[tri][idx]['no'])+1))
                else:
                    r.append(tidx.index(model_dict[tri][idx]['no']))
            else:
                leaves.append(model_dict[tri][idx]['leaf'])
                num_leaves += 1

        tobj['Tree'] = tri
        tobj['split_feature'] = [features.index(x) for x in split_feature]
        tobj['threshold'] = threshold
        tobj['right_child'] = r
        tobj['left_child'] = l
        tobj['leaf_value'] = leaves
        tobj['num_leaves'] = len(leaves)
        tobj['decision_type'] = [2]*len(threshold)

        scanned_model_dict['trees'].append(tobj)
    ##########################################################################
    return scanned_model_dict
    


def readfile(path):
    file1 = open(path, 'r')
    Lines = file1.readlines()
    stripped_lines = []
    for i in Lines:
        stripped_lines.append(i.strip())
    return stripped_lines

def extract(model):
    line = model
    main_key = None
    final = {}
    num_leaves = []
    for i in line:
        key = i.split(":")[0].split("[")
        value = i.split(":")[1:]
        if key[0] == 'booster':
            index = key[1].split("]")[0]
            main_key = int(index)
            final[main_key] = {}
            num_leaves.append(0)
        else:
            numkey = int(key[0])
            formatted_value = value[0].split(" ")
            final[main_key][numkey] = {}
            if formatted_value[0].split("=")[0] == "leaf":
                x = float(formatted_value[0].split("=")[1])
                final[main_key][numkey]["leaf"] = x
                num_leaves[main_key] += 1
            else :    
                key2 = formatted_value[0]
                val2 = formatted_value[1]
                # print(key2[1:][:-1])
                idx, tresh = key2[1:][:-1].split("<")
                tresh = float(tresh)
                yes, no, missing = val2.split(",")
                yes = int(yes.split("=")[1])
                no = int(no.split("=")[1])
                missing = int(missing.split("=")[1])
                
                final[main_key][numkey]={"index":idx,"tresh":tresh,"yes":yes,"no":no,"missing":missing}


    return final

