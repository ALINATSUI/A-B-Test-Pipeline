def clean_data(data):
    """
    TODO: Implement your "clean_heartrate_data" function from TLAB #1 & #2
    within this module. Note that this code will be *slightly* different
    from your original function.
    """
    clean_data = []
    
    for row in data:
        if row != "minutes\n":
            clean_data.append(float(row.strip()))
    return clean_data

    # using replace method
    # for row in data:
    #     row.replace('\n','')
    #     if row.isdigit():
    #         clean_data.append(row)
            
    # return clean_data        

    #using slicing method
    # sliced_data = data.slice[1:-1]
    # for row in sliced_data:
    #     row.replace('\n', '')
    #     if row.isdigit():
    #         clean_data.append(row)

    # return clean_data        

