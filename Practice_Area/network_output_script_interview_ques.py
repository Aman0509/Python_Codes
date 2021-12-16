import re
import time


def convert_nw_output_regex(output):
    start = time.time()
    output_list = re.findall(r"(\w+.*)", output)
    output_list = [i.split() for i in output_list]
    output_list[0] = [i.lower() for i in output_list[0]]
    rendered_list = []
    for i in range(1, len(output_list)):
        rendered_list.append(dict(zip(output_list[0], output_list[i])))
    end = time.time()
    print(f"Execution time - {end - start}\n")
    return rendered_list


def convert_nw_output_str(output):
    """
    This function expect that network output has the set format. Any change
    in the format will result to Exception
    """
    start = time.time()
    output_list = output.split()
    if len(output_list) % 3 == 0:
        rendered_list = []
        i = 6
        while i <= len(output_list) - 3:
            temp_dict = dict()
            temp_dict[output_list[0].lower()] = output_list[i]
            temp_dict[output_list[1].lower()] = output_list[i + 1]
            temp_dict[output_list[2].lower()] = output_list[i + 2]
            rendered_list.append(temp_dict)
            i += 3
    else:
        raise Exception("invalid network output format")
    end = time.time()
    print(f"Execution time - {end - start}\n")
    return rendered_list


if __name__ == "__main__":
    network_output = '''

    Mod         Model          Status

    --- --------------------- ---------

    1   N9K-X9636PQ           ok       

    3   N9K-X9564PX           ok       

    4   N9K-X9464TX           fail       

    21  N9K-C9504-FM          ok       

    22  N9K-C9504-FM          ok       

    23  N9K-C9504-FM          ok       

    24  N9K-C9504-FM          ok       

    25  N9K-C9504-FM          ok       

    26  N9K-C9504-FM          ok  

    '''

    network_output1 = '''
    Mod         Model          Status
    --- --------------------- ---------
    1   N9K-X9636PQ           ok       
    3   N9K-X9564PX           ok       
    4   N9K-X9464TX           fail       
    21  N9K-C9504-FM          ok       
    22  N9K-C9504-FM          ok       
    23  N9K-C9504-FM          ok       
    24  N9K-C9504-FM          ok       
    25  N9K-C9504-FM          ok       
    26  N9K-C9504-FM          ok 

    '''

    print(convert_nw_output_regex(network_output), end="\n\n")
    print("====================================================\n")
    print(convert_nw_output_str(network_output))
