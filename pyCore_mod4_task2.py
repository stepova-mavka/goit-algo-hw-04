def get_cats_info(path=str()):
    cat_data = []
    try :
        with open(path, "r", encoding="utf-8") as fh:
            while True:
                line_data = str(fh.readline())

                if line_data == '':
                    break

                split_data = line_data.split(',') # [id, name, age]

                for i in range(len(split_data)):
                    split_data[i] = split_data[i].strip() # stripping spaces and line breaks

                cat = {"id" : split_data[0], 
                    "name" : split_data[1], 
                    "age" : split_data[2]}
                
                cat_data.append(cat)

    except FileNotFoundError:
        return 'Error - file not found!'
    else:
        return cat_data

cats_info = get_cats_info('D:/basic-projects/goit-algo-hw-04/cat-data.txt')

print(cats_info)